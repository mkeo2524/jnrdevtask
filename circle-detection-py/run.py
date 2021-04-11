"""
This file is used to solve each problem
given in the task. 
"""

import sys
import runTask as rt
import getopt
'''
pair 1-12
for runP1 
python run.py problem pair image# P3SET
python run.py   P1,2or3    1-12  A or B  1,2 or 3
'''
def validate_inputs(params):
    print('')
    return 

if __name__ == "__main__":
    problem_num = None
    pair = None
    image_num = None
    P3_test = None
    validate_inputs(sys.argv)
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, '', ["problem_num =",
                                          "pair =",
                                          "image_num =",
                                          "P3_test ="])
    print(args)
    print(opts)
    # define pair
    pair = 'pair11'

    # define A or B (for runP1)
    imageNo = 'B'

    # define image set (for runP3)
    # 2 is used for pair4-7
    # 3 is used for pair8-12
    imSet = '3'

    # define which problem to solve
    p = 1
'''
    if p == 1:
        rt.runP1(pair, imageNo)
    elif p == 2:
        rt.runP2(pair)
    else:
        rt.runP3(pair,imSet)
    rt.runP1(pair, imageNo) if p == 1 else rt.runP2(pair) if p == 2 else rt.runP3(pair, imSet)
'''
