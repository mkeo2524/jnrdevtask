import numpy as np
from pathlib import Path
import random as ra
import os
from cv2 import cv2
from runTask import solveProblem1

def generateTestList(radLen):
    '''
    This function generates dummy test data for the findCentre unit it.
    inputs:  length of calculated image's radius list
    
    outputs: np.asarray(cenList): 2xn array of random centre coordinate values 
             radList: list of random radius values
    '''
    cenList = []
    radList = []

    # create a list of random floats based on the length of the input image
    for i in range(radLen):
        cenList.append([ra.random() * 1000, ra.random() * 1000])
        radList.append(ra.random() * 100)
        
    return np.asarray(cenList), radList

def getCSV(pair, im):
    '''
    This function takes in an input image pair and image number and 
    returns the directory of the test and output csv files for Problem1
    '''
    
    testDir = os.path.join(os.getcwd(),'data','P1_csv','pair' + pair,'pos_rad_' + im + '.csv')
    resultDir = os.path.join(os.getcwd(),'output', 'pair'+ pair,'pos_rad_' + im + '.csv')
    
    return testDir, resultDir

def getImage():
    '''
    This function returns a list of test images for the findCentre unit test
    The images are returned as a list
    '''
    
    dir_list = ['test_pair1', 'test_pair2', 'test_pair3']
    im_list = []

    for dir in dir_list:
        im_A = os.path.join(os.path.dirname(os.getcwd()),'testing', 'data', dir, 'figure_'+'A'+'.bmp')
        im_B = os.path.join(os.path.dirname(os.getcwd()),'testing', 'data', dir, 'figure_'+'B'+'.bmp')
        im_list.append(cv2.imread(im_A))
        im_list.append(cv2.imread(im_B))
        
    return im_list

def getImageDir():
    '''
    This function gets the image directories of the images being used in the solveProblem1 unit test
    The image directories are returned as a list
    '''
    
    dir_list = ['test_pair1', 'test_pair2', 'test_pair3']
    im_list = []

    for dir in dir_list:
        im_A = os.path.join(os.path.dirname(os.getcwd()),'testing', 'data', dir, 'figure_'+'A'+'.bmp')
        im_B = os.path.join(os.path.dirname(os.getcwd()),'testing', 'data', dir, 'figure_'+'B'+'.bmp')
        im_list.append(im_A)
        im_list.append(im_B)
        
    return im_list
    

