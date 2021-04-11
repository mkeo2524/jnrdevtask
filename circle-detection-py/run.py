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
def validate_inputs(opts, args):
    problem_num = None
    pair = None
    image_num = None
    T3_test = None
    
    # obtain argument values
    for opt, arg in opts:
        print(opt)
        if opt == "--problem_num":
            problem_num = arg
        elif opt == "--pair":
            pair = "pair" + arg
        elif opt == "--image_num":
            image_num = arg
        elif opt == "--T3_test":
            T3_test = arg
    
    
    return 

if __name__ == "__main__":
    
    
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, '', ["problem_num=",
                                          "pair=",
                                          "image_num=",
                                          "T3_test="])
    validate_inputs(opts, args)
    
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
