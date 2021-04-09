"""
this module manages lower level functions to
run the optimizations. 
"""

import sys
import time
from numpy import *
import numpy as np
from math import sqrt
import scipy
import cv2
from scipy.spatial import distance as dist
from scipy.spatial import cKDTree
from scipy.optimize import leastsq, fmin
from scipy import optimize
from scipy.linalg import lstsq
import imutils
from imutils import perspective
from imutils import contours
import matplotlib

gui_env = ['TKAgg', 'GTKAgg', 'Qt4Agg', 'WXAgg']
for gui in gui_env:
    try:
        # ~ print "testing", gui
        matplotlib.use(gui, warn=False, force=True)
        from matplotlib import pyplot as plt

        break
    except:
        continue
# ~ print "Using:",matplotlib.get_backend
import pdb


def findImageSize(image):
    """
    find image height and width
    """

    return image.shape[:2]


def findCentre(image):
    """
    find centre of the circles. 
    
    Input = image file
    Output = mx2 array 
    """

    edged = cv2.Canny(image, 50, 100)
    imcopy = edged.copy()

    # find circles and sort them
    crcl = cv2.findContours(imcopy, cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    if imutils.is_cv2():
        crcl = crcl[0]
    else:
        crcl = crcl[1]
    (crcl, _) = contours.sort_contours(crcl)

    # loop over each circle
    numCircles = 0
    centreList = []
    radiusList = []
    for circles in crcl:
        numCircles += 1
        bbox = cv2.minAreaRect(circles)
        if imutils.is_cv2():
            bbox = cv2.cv.BoxPoints(bbox)
        else:
            bbox = cv2.boxPoints(bbox)
        bbox = np.array(bbox, dtype='int')
        bbox = perspective.order_points(bbox)
        (c1, c2, c3, c4) = bbox

        midc12 = (c1 + c2) * 0.5
        midc34 = (c3 + c4) * 0.5
        c = (midc12 + midc34) * 0.5
        centreList.append(c)
        radius = (dist.euclidean((midc12[0], midc12[1]), (midc34[0], midc34[1]))) * 0.5
        # ~ im = plt.imread(image)
        # ~ implot = plt.imshow(image)
        # ~ plt.scatter(c[0], c[1], s=10)
        radiusList.append(radius)
    centreList = np.asarray(centreList)

    # ~ plt.show(0)

    return centreList, radiusList


def optimizeCircleLSQ1(X, Y, radiusListA, radiusListB, im1Size, im2Size, xtol=1e-03, maxfev=10):
    D = X
    T = Y

    radiusListA = np.array(radiusListA)
    radiusListB = np.array(radiusListB)

    t0 = scipy.array([0.0, 0.0, 0.0, 1.0])

    TTree = cKDTree(T)
    D = scipy.array(D)

    def obj(t):

        transformedData = affine2DAboutCoI(X, t, im1Size)
        dataTree = cKDTree(transformedData)
        dD, di = dataTree.query(Y)
        dDRad = radiusListA[di] - radiusListB
        dT, ti = TTree.query(transformedData)
        dTRad = radiusListB[ti] - radiusListA
        dDSortedIndexs = np.argsort(dD)
        dTSortedIndexs = np.argsort(dT)

        lb = 0
        ub = 1
        dD = np.array(dD)[dDSortedIndexs][int(len(dD) * lb):int(len(dD) * ub)]
        dT = np.array(dT)[dTSortedIndexs][int(len(dT) * lb):int(len(dT) * ub)]
        dDRad = np.array(dDRad)[dDSortedIndexs][int(len(dDRad) * lb):int(len(dDRad) * ub)]
        dTRad = np.array(dTRad)[dTSortedIndexs][int(len(dTRad) * lb):int(len(dTRad) * ub)]

        # return (dD*dD).mean()+(dT*dT).mean()+(dDRad*dDRad).mean()+(dTRad*dTRad).mean()
        return (dD*dD)+(dT*dT)+(dDRad*dDRad)+(dTRad*dTRad)

    def index(t):
        D1 = cKDTree(D)
        T1 = cKDTree(T)
        _, indexes1 = D1.query(X)
        _, indexes2 = T1.query(Y)
        return indexes1, indexes2

    initialRMSE = scipy.sqrt(obj(t0).mean())
    i1, i2 = index(t0)
    print('\nOptimising...')
    minima = []
    reses = []
    tot_itt = 50

    for rot in np.linspace(0, 360, 1000):
        t0 = scipy.array([0.0, 0.0, np.deg2rad(rot), 1.0])
        # res = scipy.optimize.minimize(obj, t0, method='Nelder-Mead',
        #                               options={'disp': False, 'xatol': 1e-4, 'fatol': 1e-4, 'maxiter': 1e6})
        # tOpt = res.x
        minima.append(obj(t0))
        reses.append(rot)



        #tOpt = leastsq(obj, t0, xtol=xtol, maxfev=maxfev)[0]
        #finalRMSE = scipy.sqrt(obj(tOpt).mean())
        #minima.append(finalRMSE)
        #reses.append(tOpt)

    plt.plot(minima, reses)
    plt.show()
    # tOpt = reses[minima.index(min(minima))]
    # data = affine2DAboutCoI(D, tOpt, im1Size)
    # plt.scatter(data[:, 0], data[:, 1], s=100,c='red', alpha=0.5)
    sys.exit()
    # print min(minima)
    return tOpt, initialRMSE, min(minima), i1, i2, data


def optimizeCircleLSQ2(X, Y, radiusListA, radiusListB, im1Size, im2Size, xtol=0.00001, maxfev=0):
    D = X
    T = Y

    radiusListA = np.array(radiusListA)
    radiusListB = np.array(radiusListB)

    t0 = scipy.array([0.0, 0.0, 0.0, 1.0])

    TTree = cKDTree(T)
    D = scipy.array(D)

    def obj(t):

        transformedData = affine2DAboutCoI(X, t, im1Size)
        dataTree = cKDTree(transformedData)
        dD, di = dataTree.query(Y)
        dDRad = radiusListA[di] - radiusListB
        dT, ti = TTree.query(transformedData)
        dDSortedIndexs = np.argsort(dD)
        dTSortedIndexs = np.argsort(dT)

        lb = 0
        ub = 1
        dD = np.array(dD)[dDSortedIndexs][int(len(dD) * lb):int(len(dD) * ub)]
        dT = np.array(dT)[dTSortedIndexs][int(len(dT) * lb):int(len(dT) * ub)]
        dDRad = np.array(dDRad)[dDSortedIndexs][int(len(dDRad) * lb):int(len(dDRad) * ub)]

        return (dD*dD)+(dDRad*dDRad)

    def index(t):
        D1 = cKDTree(D)
        T1 = cKDTree(T)
        _, indexes1 = D1.query(X)
        _, indexes2 = T1.query(Y)
        return indexes1, indexes2

    initialRMSE = scipy.sqrt(obj(t0).mean())
    i1, i2 = index(t0)
    minima = []
    reses = []
    for rot in np.linspace(0, 360, 50):
        t0 = scipy.array([0.0, 0.0, np.deg2rad(rot), 1.0])
        tOpt = leastsq(obj, t0, xtol=xtol, maxfev=maxfev)[0]
        finalRMSE = scipy.sqrt(obj(tOpt).mean())
        minima.append(finalRMSE)
        reses.append(tOpt)

    tOpt = reses[minima.index(min(minima))]
    data = affine2DAboutCoI(D, tOpt, im1Size)
    return tOpt, initialRMSE, min(minima), i1, i2, data


def optimizeCircleNLDRMD(X, Y, radiusListA, radiusListB, im1Size, im2Size, xtol=0, maxfev=0):
    D = X
    T = Y

    radiusListA = np.array(radiusListA)
    radiusListB = np.array(radiusListB)

    t0 = scipy.array([0.0, 0.0, 0.0, 1.0])

    TTree = cKDTree(T)
    D = scipy.array(D)

    def obj(t):

        transformedData = affine2DAboutCoI(X, t, im1Size)
        dataTree = cKDTree(transformedData)
        dD, di = dataTree.query(Y)
        dDRad = radiusListA[di] - radiusListB
        dT, ti = TTree.query(transformedData)
        dTRad = radiusListB[ti] - radiusListA
        dDSortedIndexs = np.argsort(dD)
        dTSortedIndexs = np.argsort(dT)

        lb = 0
        ub = 0.8
        dD = np.array(dD)[dDSortedIndexs][int(len(dD) * lb):int(len(dD) * ub)]
        dT = np.array(dT)[dTSortedIndexs][int(len(dT) * lb):int(len(dT) * ub)]
        dDRad = np.array(dDRad)[dDSortedIndexs][int(len(dDRad) * lb):int(len(dDRad) * ub)]
        dTRad = np.array(dTRad)[dTSortedIndexs][int(len(dTRad) * lb):int(len(dTRad) * ub)]

        return (dD*dD).mean()+(dT*dT).mean()+(dDRad*dDRad).mean()+(dTRad*dTRad).mean()

    obj(t0)

    def index(t):
        D1 = cKDTree(D)
        T1 = cKDTree(T)
        _, indexes1 = D1.query(X)
        _, indexes2 = T1.query(Y)
        return indexes1, indexes2

    initialRMSE = scipy.sqrt(obj(t0).mean())
    i1, i2 = index(t0)
    minima = []
    reses = []
    for rot in np.linspace(0, 360, 1000):
        t0 = scipy.array([0.0, 0.0, np.deg2rad(rot), 1.0])
        res = scipy.optimize.minimize(obj, t0, method='Nelder-Mead',
                                      options={'disp': False, 'xatol': 1e-5, 'fatol': 1e-4, 'maxiter': 1e6})
        minima.append(obj(t0))
        reses.append(rot)
        tOpt = res.x

    plt.plot(minima, reses)
    plt.show()
    sys.exit()
    tOpt = reses[minima.index(min(minima))]
    data = affine2DAboutCoI(D, tOpt, im1Size)

    return tOpt, initialRMSE, min(minima), i1, i2, data


def affine2DAboutCoI(x, t, im1Size):
    xO = x - array(im1Size) / 2
    xOT = affine2DRigid(xO, t)

    return xOT + array(im1Size) / 2


def affine2DRigid(x, t):
    """ 
    applying a rigid transformation.
    
    """


    # initializing T matrix (tx,ty,rx,s)
    T = scipy.array([[1.0, 0.0, t[0]], \
                     [0.0, 1.0, t[1]], \
                     [1.0, 1.0, 1.0]])

    Rx = scipy.array([
        [scipy.cos(t[2]), -scipy.sin(t[2])], \
        [scipy.sin(t[2]), scipy.cos(t[2])]])

    T[:2, :2] = Rx
    temp = scipy.dot(T, X)[:2, :].T
    return scipy.multiply(temp, t[3])

def cpd(X, Y):
    from functools import partial
    from scipy.io import loadmat
    from pycpd import rigid_registration

    fig = plt.figure()
    fig.add_axes([0, 0, 1, 1])
    callback = partial(visualize, ax=fig.axes[0])

    reg = rigid_registration(X, Y, maxIterations=100, tolerance=0.0001)
    reg.tolerance = 1e-6
    reg.register(callback)
    plt.scatter(reg.TY[:,0], reg.TY[:,1], s=100, alpha=0.5)
    plt.scatter(X[:, 0], X[:, 1], s=100,c='red', alpha=0.5)

    return reg.R, reg.t, reg.s

def visualize(iteration, error, X, Y, ax):
    plt.cla()
    ax.scatter(X[:, 0], X[:, 1], color='red')
    ax.scatter(Y[:, 0], Y[:, 1], color='blue')
    plt.draw()
    print("iteration %d, error %.10f" % (iteration, error))
    plt.pause(0.001)
    # plt.savefig('image/%d.jpg' %(iteration))
