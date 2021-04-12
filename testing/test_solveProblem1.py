import unittest
import os
from cv2 import cv2
import numpy as np
from testHelper import getCSV, getImage, getImageDir
from runTask import solveProblem1
from difflib import Differ

class TestFindCentre(unittest.TestCase):
    
    def test_pair1_A(self):
        imageDir = getImageDir()
        solveProblem1(imageDir[0], 'pair1', 'A')
        testDir, resultDir = getCSV('1', 'A')

        with open(testDir, 'r') as dir1, open(resultDir, 'r') as dir2:
            csv1 = dir1.readlines()
            csv2 = dir2.readlines()
            for line in csv2:
                self.assertNotIn(line, csv1)

    def test_pair1_B(self):
        imageDir = getImageDir()
        solveProblem1(imageDir[0], 'pair1', 'B')
        testDir, resultDir = getCSV('1', 'B')
        
        with open(testDir, 'r') as dir1, open(resultDir, 'r') as dir2:
            csv1 = dir1.readlines()
            csv2 = dir2.readlines()
            for line in csv2:
                self.assertNotIn(line, csv1)
    
    def test_pair2_A(self):
        imageDir = getImageDir()
        solveProblem1(imageDir[0], 'pair2', 'A')
        testDir, resultDir = getCSV('2', 'A')

        with open(testDir, 'r') as dir1, open(resultDir, 'r') as dir2:
            csv1 = dir1.readlines()
            csv2 = dir2.readlines()
            for line in csv2:
                self.assertNotIn(line, csv1)
                
    def test_pair2_B(self):
        imageDir = getImageDir()
        solveProblem1(imageDir[0], 'pair2', 'B')
        testDir, resultDir = getCSV('2', 'B')

        with open(testDir, 'r') as dir1, open(resultDir, 'r') as dir2:
            csv1 = dir1.readlines()
            csv2 = dir2.readlines()
            for line in csv2:
                self.assertNotIn(line, csv1)
                
    def test_pair3_A(self):
        imageDir = getImageDir()
        solveProblem1(imageDir[0], 'pair3', 'A')
        testDir, resultDir = getCSV('3', 'A')
        
        with open(testDir, 'r') as dir1, open(resultDir, 'r') as dir2:
            csv1 = dir1.readlines()
            csv2 = dir2.readlines()
            for line in csv2:
                self.assertNotIn(line, csv1)
        
    def test_pair3_B(self):
        imageDir = getImageDir()
        solveProblem1(imageDir[0], 'pair3', 'B')
        testDir, resultDir = getCSV('3', 'B')
        
        with open(testDir, 'r') as dir1, open(resultDir, 'r') as dir2:
            csv1 = dir1.readlines()
            csv2 = dir2.readlines()
            for line in csv2:
                self.assertNotIn(line, csv1)
                
if __name__ == '__main__':
    unittest.main()

