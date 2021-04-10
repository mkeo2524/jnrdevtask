"""
This file is used to solve each problem
given in the task. 
"""

import sys
import runTask as rt
'''
pair 1-12
for runP1 

'''
def validate_inputs(params):
    print('')
    return 

if __name__ == "__main__":
    
    validate_inputs(sys.argv)
    # define pair
    pair = 'pair1'

    # define A or B (for runP1)
    im = 'B'

    # define image set (for runP3)
    # 2 is used for pair4-7
    # 3 is used for pair8-12
    imSet = '3'

    # define which problem to solve
    p = 1

    if p == 1:
        rt.runP1(pair, im)
    elif p == 2:
        rt.runP2(pair)
    else:
        rt.runP3(pair,imSet)
    rt.runP1(pair, im) if p == 1 else rt.runP2(pair) if p == 2 else rt.runP3(pair, imSet)

