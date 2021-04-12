"""
this module manages higher level functions to
run the optimizations. 
"""

import numpy as np
import math
import time
from cv2 import cv2
import sys
import tools
# reload (tools)
import matplotlib
import os.path


gui_env = ['TKAgg','GTKAgg','Qt4Agg','WXAgg']
for gui in gui_env:
    try:
        matplotlib.use(gui,warn=False, force=True)
        from matplotlib import pyplot as plt
        break
    except:
        continue

def solveProblem1( im, pair, img ):
    image = cv2.imread(im)
    p, r = tools.findCentre(image)
    outputDir = 'output/'+pair+'/'

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    
    file = open(outputDir+'/pos_rad_'+img+'.csv', "w")
    file.write('Circle, Position (x y), Radius (px)\n')
    with open(outputDir+'/pos_rad_'+img+'.csv', "a") as csv_file:
        numCircles = 0
        for data in range(len(p)):
            numCircles+=1
            file.write('%.0f , (%.0f %.0f), %.2f\n' 
            % (numCircles, p[data][0],p[data][1], r[data]))
    file.close()
    return None
   
def solveProblem2( im1, im2, pair ):
    import os
    import math
    tic = time.perf_counter()
    image1 = cv2.imread(im1)
    image2 = cv2.imread(im2)
    d1,radiusListA = tools.findCentre(image1)
    d2,radiusListB = tools.findCentre(image2)
    
    im1Size = tools.findImageSize(image1)
    im2Size = tools.findImageSize(image2)

    T, inrms, rms, ind, i2, data = tools.optimizeCircleLSQ1(d1, d2, radiusListA, radiusListB, im1Size, im2Size)
    R, t, s = tools.cpd(data, d2)
    tform1 = T
    tform2 = [t[0], t[1], math.acos(R[0][0]), s]

    toc = time.perf_counter()
    totTime = toc - tic
    print('Done!')
    print('Total time = %.4f s' % totTime)
    outputDir = 'output/'+pair+'/'
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
        
    file = open(outputDir+'/pos_imA_imB.csv', "wb")
    file.write('Circle, ImA (x y), ImB (x y)\n')
    #~ file.close()
    with open(outputDir+'/pos_imA_imB.csv', "a") as csv_file:   
        numCircles = 0
        for i in range(len(ind)):
            numCircles+=1
            file.write('%.0f, %.0f %.0f , %.0f %.0f\n' 
            % (numCircles, d1[ind][i][0], d1[ind][i][1],
                        d2[ind][i][0], d2[ind][i][1]))
    warpImage( im1, tform1, tform2, pair)
    
    file = open(outputDir+'/transformation.txt', "wb")
    file.write("The global transformation: \n")
    file.write("[ t_x   t_y   r   s]\n")
    file.write('[%.4f, %.4f, %.4f, %.4f]\n' 
                %(T[0], T[1], T[2], T[3]))
    file.close()
    print("=========")
    print("The global transformation: ")
    print("[ t_x   t_y   r   s]")
    print(T)

    return T,
    
def solveProblem3( im1, im2, imSet, pair ):
    import os
    tic = time.perf_counter()
    image1 = cv2.imread(im1)
    image2 = cv2.imread(im2)
    d1,radiusListA = tools.findCentre(image1)
    d2,radiusListB = tools.findCentre(image2)
    
    im1Size = tools.findImageSize(image1)
    im2Size = tools.findImageSize(image2)

    print('\nOptimising...')
    if imSet == '2':
        T, inrms, rms, ind, i2, data = tools.optimizeCircleLSQ2(d1, d2, radiusListA, radiusListB, im1Size, im2Size)
        R, t, s = tools.cpd(data, d2)
        tform = T
        T2 = [t[0], t[1], math.acos(R[0][0]), s]
        tform2 = T2

        toc = time.perf_counter()
        totTime = toc - tic
        print('Done!')
        print('Total time = %.4f s' % totTime)
        outputDir = 'output/'+pair+'/'
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)

        file = open(outputDir+'/pos_imA_imB.csv', "wb")
        file.write('Circle, ImA (x y), ImB (x y)\n')
        with open(outputDir+'/pos_imA_imB.csv', "a") as csv_file:   
            numCircles = 0
            if len(ind) > len(i2):
                for i in range(len(i2)):
                    numCircles+=1
                    file.write('%.0f, %.0f %.0f , %.0f %.0f\n' 
                    % (numCircles, d1[i2][i][0], d1[i2][i][1],
                            d2[i2][i][0], d2[i2][i][1]))
            else:
                for i in range(len(ind)):
                    numCircles+=1
                    file.write('%.0f, %.0f %.0f , %.0f %.0f\n' 
                    % (numCircles, d1[ind][i][0], d1[ind][i][1],
                            d2[ind][i][0], d2[ind][i][1]))
        warpImage( im1, tform, tform2, pair )
        file = open(outputDir+'/transformation.txt', "wb")
        file.write("The global transformation: \n")
        file.write("[ t_x   t_y   r   s]\n")
        file.write('[%.4f, %.4f, %.4f, %.4f]\n'
                    %(T[0], T[1], T[2], T[3]))
        file.close()
        print("=========")
        print("The global transformation: ")
        print("[ t_x   t_y   r   s]")
        print(T)
        return T
    elif imSet == '3':
        T, inrms, rms, ind, i2, data = tools.optimizeCircleNLDRMD(d1, d2, radiusListA, radiusListB, im1Size, im2Size)
        R, t, s = tools.cpd(data, d2)
        tform = T
        T2 = [t[0], t[1], math.acos(R[0][0]), s]

        tform2 = T2
        toc = time.perf_counter()
        elapsedTime = toc - tic
        print('Done!')
        print('Total time = %.4f s' % elapsedTime)
        outputDir = 'output/'+pair+'/'
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)
        
        file = open(outputDir+'/pos_imA_imB.csv', "wb")
        file.write('Circle, ImA (x y), ImB (x y)\n')
        with open(outputDir+'/pos_imA_imB.csv', "a") as csv_file:   
            numCircles = 0
            if len(ind) > len(i2):
                for i in range(len(i2)):
                    numCircles+=1
                    file.write('%.0f, %.0f %.0f , %.0f %.0f\n' 
                    % (numCircles, d1[i2][i][0], d1[i2][i][1],
                            d2[i2][i][0], d2[i2][i][1]))
            else:
                for i in range(len(ind)):
                    numCircles+=1
                    file.write('%.0f, %.0f %.0f , %.0f %.0f\n' 
                    % (numCircles, d1[ind][i][0], d1[ind][i][1],
                            d2[ind][i][0], d2[ind][i][1]))

        warpImage( im1, tform, tform2, pair )
        file = open(outputDir+'/transformation.txt', "wb")
        file.write("The global transformation: \n")
        file.write("[ t_x   t_y   r   s]\n")
        file.write('[%.4f, %.4f, %.4f, %.4f]\n' 
                    %(T[0], T[1], T[2], T[3]))
        file.close()
        print("=========")
        print("The global transformation: ")
        print("[ t_x   t_y   r   s]")
        print(T)

        return T
    else :
        print('Wrong image set. Please choose either 2 or 3.')
        return None

def warpImage( im, tForm, tForm2, pair ):
    import os
    from skimage import transform
    img = cv2.imread(im)

    shift_y, shift_x = np.array(img.shape[:2]) / 2
    tf_rotate = transform.SimilarityTransform(rotation=tForm[2])
    tf_shift = transform.SimilarityTransform(translation=[-shift_x, -shift_y])
    tf_shift_inv = transform.SimilarityTransform(translation=[shift_x, shift_y])

    image_rotated = transform.warp(img, ((tf_shift) +
                (tf_rotate + tf_shift_inv)).inverse)

    shift_y, shift_x = np.array(img.shape[:2]) / 2
    tf_rotate_1 = transform.SimilarityTransform(rotation=tForm2[2])
    tf_shift_1 = transform.SimilarityTransform(translation=[-shift_x, -shift_y])
    tf_shift_inv_1 = transform.SimilarityTransform(translation=[shift_x, shift_y])

    image_rotated_1 = transform.warp(image_rotated, ((tf_shift_1) +
                (tf_rotate_1 + tf_shift_inv_1)).inverse)

    fig, ax = plt.subplots(nrows=1)

    ax.imshow(image_rotated_1)

    outputDir = 'output/'+pair+'/'
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
 
    plt.savefig(outputDir+'warpA.jpg')
    
    return None

def runP1( pair, img ):
    
    # create path of image
    filePath = os.path.join(os.path.dirname(os.getcwd()), 'circle-detection-and-registration', 'data', pair, 'figure_'+img+'.bmp')
    solveProblem1( filePath, pair, img )
    return None
    
def runP2( pair ):
    
    # define file paths for images A & B
    imfile1 = os.path.join(os.path.dirname(os.getcwd()), 'circle-detection-and-registration', 'data', pair, 'figure_A.bmp')
    imfile2 = os.path.join(os.path.dirname(os.getcwd()), 'circle-detection-and-registration', 'data', pair, 'figure_B.bmp')
    solveProblem2( imfile1, imfile2, pair )

    return None
    
def runP3( pair, imSet ):
    
    # define file paths for images A & B
    imfile1 = os.path.join(os.path.dirname(os.getcwd()), 'circle-detection-and-registration', 'data', pair, 'figure_A.bmp')
    imfile2 = os.path.join(os.path.dirname(os.getcwd()), 'circle-detection-and-registration', 'data', pair, 'figure_B.bmp')
    solveProblem3( imfile1, imfile2, imSet, pair )
    
    return None