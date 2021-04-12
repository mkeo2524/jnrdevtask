JNRDEVTASK
########################################################################################
jnrdevtask is coding task set to ABI junior developer candidates. The project consists of 
improving a script to run three problems. More info. on the problems can be found in 
./circle-detection-and-registration/Instruction.pdf

HOW TO USE
########################################################################################

RUNNING THE SCRIPT
########################################################################################
All three problems can be run from ./circle-detection-py/run.py

The script takes in specific parameters when run on the command line.

Parameters:

1.  --problem_num: 
    Description: The number of the problem being solved. (Mandatory)
    Input method: 1, 2, or 3
2.  --pair:  
    Description: The image pair being solved. (Mandatory)
    Input method: A or B
3. --image_num: 
    Description: The image between the pair being tested; required to solve Problem 1.
    Input method: 0 to 12 inclusive
4. --T3_test: 
    Description: The image set being tested for Problem 3.
    Input method: 1, 2 or 3

CODE EXAMPLE
########################################################################################

1. Running Problem 1

 This code will run problem 1 on image B of image pair 6:

python run.py --problem_num 1 --pair 6 --image_num B

2. Running Problem 2

 This code will run problem 2 on image pair 11

python run.py --problem_num 2 --pair 11

3. Running Problem 3

 This code will run problem 3 on image pair 8 using test set 2

python run.py --problem_num 3 --pair 8 --T3_test 2

TEST
########################################################################################

unittests for Problem 1 can be found in ./testing

Running individual test scripts can be done with the command:

python 'script_name'.py

Running all tests can be done with the command:

python -m unittest discover

NOTE
########################################################################################
1. The script can only test one problem per run
2. The script can only be run on a single image and pair per run for problem 1
3. The script can only be run on a single image pair for problem 2
4. The script can only be run on a single test set and image pair for problem 3
5. The script currently only runs on the skeleton image pairs provided (pair0 - pair12)
6. The script currently only supports .BMP images
5. Changing the project directory structure or file and folder naming may break the code
6. The circle-detection-py directory must be on the PYTHONPATH for the testing to run

INSTALLATION
########################################################################################
Run this command on the command line:

  pip install -r requirements.txt

CONTRIBUTE
########################################################################################
You may contribute if you wish but the project will be discontinued after 5 p.m 13/04/2021

GITHUB: https://github.com/mkeo2524/jnrdevtask