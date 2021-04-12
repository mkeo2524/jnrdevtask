import numpy as np

import random as ra
cenList = []
radList = []

def generateTestList(radLen):
    for i in range(radLen):
        cenList.append([ra.random() * 1000, ra.random() * 1000])
        radList.append(ra.random() * 100)
    return np.asarray(cenList), radList

