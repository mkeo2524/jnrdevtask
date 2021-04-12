import unittest
import os
from tools import findCentre
from cv2 import cv2
from centreData import generateTestList
import numpy as np

dir_list = ['test_pair0', 'test_pair1', 'test_pair2']
im_list = []

for dir in dir_list:
    im_A = os.path.join(os.path.dirname(os.getcwd()),'testing', 'data', dir, 'figure_'+'A'+'.bmp')
    im_B = os.path.join(os.path.dirname(os.getcwd()),'testing', 'data', dir, 'figure_'+'B'+'.bmp')
    im_list.append(cv2.imread(im_A))
    im_list.append(cv2.imread(im_B))

class TestFindCentre(unittest.TestCase):
    
    def test_pair0_A(self):
        self.result_centre_list, self.result_radius_list = findCentre(im_list[0])
        test_centre_list, test_radius_list = generateTestList(len(self.result_radius_list))
        np.alltrue(test_centre_list == self.result_centre_list)
        self.assertListEqual(test_radius_list, self.result_radius_list)

    
  
if __name__ == '__main__':
    unittest.main()

