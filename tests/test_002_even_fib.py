""" Test class for ex_002_even_fib"""
import unittest
from itertools import takewhile
from src import ex_002_even_fib as mut # mut = Module Under Test

class Test001Multiples(unittest.TestCase):
    """ Test class for Tex_002_even_fib """
    def test_generator(self):
        """ Test the fibonacci generator"""
        less_than_90 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        generated = [fib_no for fib_no in takewhile(lambda x: x < 90, mut.fibonacci_generator())]
        self.assertTrue(less_than_90 == generated,
                        "Equals failed generated vs Hard coded {0}".format(generated))

    def test_sum_of_even(self):
        """ Tests the sum_of_even_fibonacci_numbers method """
        # Even fib numbers below 90 are 2 8 34
        evensum = 2 + 8 + 34
        mutsum = mut.sum_of_even_fibonacci_numbers(90)
        self.assertEqual(evensum, mutsum,
                         "Incorrect sum, expected {0} got {1}".format(evensum, mutsum))

    def test_main(self):
        """ Tests the main method, compares to the correct Euler answer 4613732"""
        answer = 4613732
        mut_answer = mut.run_main()
        self.assertEqual(answer, mut_answer,
                         "Main calculation incorrect, got {} expected {}"
                         .format(mut_answer, answer))

if __name__ == '__main__':
    unittest.main() # pragma: no cover
    