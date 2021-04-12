"""
This file is used to solve each problem
given in the task. 
"""

import sys
import runTask as rt
import getopt

def validate_arguments(opts):
    '''
        This function runs a simple validation on the script inputs
    '''
    problem_num = None
    pair = None
    image_num = None
    T3_test = None
    
    # obtain argument values
    for opt, arg in opts:

        if opt == "--problem_num":
            problem_num = arg
        elif opt == "--pair":
            pair = arg
        elif opt == "--image_num":
            image_num = arg
        elif opt == "--T3_test":
            T3_test = arg
    
    # test validity of script arguments
    if problem_num == None:
        raise Exception("You must input the problem number")
    elif problem_num not in ['1', '2', '3']:
        raise Exception("Problem being run must be 1, 2 or 3 and enetered in as an integer")
    
    if pair != None:
        if int(pair) not in list(range(1,13)):
            raise Exception("Image pairs must range from 1 to 12 and enetered in as an integer")
        
    if image_num != None:
        if image_num not in ["A", "B"]:
            raise Exception("You must select either image A or B by entering in A or B")
    
    if T3_test != None:
        if int(T3_test) not in list(range(1,4)):
            raise Exception("Testings options range from test 1 to test 3 and enetered in as an integer")

    # check required arguments to solve problems
    if problem_num == '1' and (pair == None or image_num == None):
        raise Exception("Please check requirements to test task 1")
    
    elif problem_num == '2' and pair == None:
        raise Exception("Please check requirements to test task 2")
    
    elif problem_num == '3' and (pair == None or T3_test == None):
        raise Exception("Please check requirements to test task 3")
    
    return problem_num, pair, image_num, T3_test

if __name__ == "__main__":
    
    argv = sys.argv[1:] # list of argument inputs
    
    opts, args = getopt.getopt(argv, '', ["problem_num=",
                                          "pair=",
                                          "image_num=",
                                          "T3_test="])
    
    problem_num, pair, image_num, T3_test = validate_arguments(opts) # argument validation
    
    # run problem based on user input
    if problem_num == '1':
        rt.runP1("pair" + pair, image_num)
    elif problem_num == '2':
        rt.runP2("pair" + pair)
    else:
        rt.runP3("pair" + pair, T3_test)


