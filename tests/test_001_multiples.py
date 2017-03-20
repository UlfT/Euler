""" Test class for ex_001_multiples"""
import unittest
from src import ex_001_multiples as mut # mut = Module Under Test


class Test001Multiples(unittest.TestCase):
    """ Test class for ex_001_multiples """

    def test_is_multiple(self):
        """ Tests the is_multiple_of_3_or_5 method"""
        self.assertTrue(mut.is_multiple_of_3_or_5(3), "Expected to see that 3 was an multiple")
        self.assertTrue(mut.is_multiple_of_3_or_5(5), "Expected to see that 5 was an multiple")
        self.assertTrue(mut.is_multiple_of_3_or_5(3*3*5*5),
                        "Expected to see that 9x25 was an multiple")
        self.assertFalse(mut.is_multiple_of_3_or_5(7), "7 should not be a multiple")

    def test_sum(self):
        """ Tests the sum_of_3_5_multiples method. Only tests for positie numbers"""
        self.assertEqual(mut.sum_of_3_5_multiples(10), 23, "Textbook example of 10 and 23 failed")

if __name__ == '__main__':
    unittest.main()

# nosestests
