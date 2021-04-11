import unittest

from run import validate_arguments

class TestValidation(unittest.TestCase):
    '''
    Tests argument input validation for run.py
    '''
    def test_problem_num(self):
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '0')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '-1')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '-4')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', 'foo')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '%@#@!')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '2')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', None)])
        
    def test_pair(self):
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', '1')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', '12')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', 1)])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', 12)])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', 'A')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', '$@%@#$')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', ' ')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None)])
    
    def test_image_num(self):
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num,', 'A')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', 'B')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', 'C')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', 'D')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', ' ')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', '1')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', 1)])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', None)])
    
    def test_T3_test(self):
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', None), ('--T3_test', '1')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', None), ('--T3_test', '2')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', None), ('--T3_test', '3')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', None), ('--T3_test', '4')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', None), ('--T3_test', '-4')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', None), ('--T3_test', 'DA')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', None), ('--T3_test', ' ')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', None), ('--T3_test', '^$%#$')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', None), ('--T3_test', 1)])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'), ('--pair', None), ('--image_num', None), ('--T3_test', None)])
    
    def test_problem1(self):
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'),('--pair', None), ('--image_num', None)])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'),('--pair', 5), ('--image_num', None)])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'),('--pair', None), ('--image_num', 'A')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'),('--pair', None), ('--image_num', 'B')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '1'),('--pair', 2), ('--image_num', None)])
    
    def test_problem2(self):
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '2'),('--pair', None)])

    def test_problem3(self):
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '3'),('--pair', None), ('--T3_test', None)])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '3'),('--pair', 5), ('--T3_test', None)])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '3'),('--pair', None), ('--T3_test', 'A')])
        self.assertRaises(Exception, validate_arguments, [('--problem_num', '3'),('--pair', None), ('--T3_test', 'B')])
        
if __name__ == '__main__':
    unittest.main()

    