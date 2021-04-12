import unittest
import os
from tools import findCentre
from cv2 import cv2
from testHelper import generateTestList, getImage

import numpy as np

im_list = getImage() # gets test image set

class TestFindCentre(unittest.TestCase):
    '''
    unit test for the findCentre function in circle-detection-py/tools.py
    tests are run on given image data set pair1 - pair 3
    no edge cases are tested
    '''
    
    def test_pair0_A(self):
        self.result_centre_list, self.result_radius_list = findCentre(im_list[0])
        test_centre_list, test_radius_list = generateTestList(len(self.result_radius_list))
        np.alltrue(test_centre_list == self.result_centre_list)
        self.assertListEqual(test_radius_list, self.result_radius_list)

    def test_pair0_B(self):
        self.result_centre_list, self.result_radius_list = findCentre(im_list[1])
        test_centre_list, test_radius_list = generateTestList(len(self.result_radius_list))
        np.alltrue(test_centre_list == self.result_centre_list)
        self.assertListEqual(test_radius_list, self.result_radius_list)
        
    def test_pair1_A(self):
        self.result_centre_list, self.result_radius_list = findCentre(im_list[2])
        test_centre_list, test_radius_list = generateTestList(len(self.result_radius_list))
        np.alltrue(test_centre_list == self.result_centre_list)
        self.assertListEqual(test_radius_list, self.result_radius_list)
        
    def test_pair1_B(self):
        self.result_centre_list, self.result_radius_list = findCentre(im_list[3])
        test_centre_list, test_radius_list = generateTestList(len(self.result_radius_list))
        np.alltrue(test_centre_list == self.result_centre_list)
        self.assertListEqual(test_radius_list, self.result_radius_list)
    
    def test_pair2_A(self):
        self.result_centre_list, self.result_radius_list = findCentre(im_list[4])
        test_centre_list, test_radius_list = generateTestList(len(self.result_radius_list))
        np.alltrue(test_centre_list == self.result_centre_list)
        self.assertListEqual(test_radius_list, self.result_radius_list)
        
    def test_pair2_B(self):
        self.result_centre_list, self.result_radius_list = findCentre(im_list[5])
        test_centre_list, test_radius_list = generateTestList(len(self.result_radius_list))
        np.alltrue(test_centre_list == self.result_centre_list)
        self.assertListEqual(test_radius_list, self.result_radius_list)
  
if __name__ == '__main__':
    unittest.main()

