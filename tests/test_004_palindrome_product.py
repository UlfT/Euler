""" Tests for ex_001_multiples"""
from nose2.tools import such
import nose2
from src import ex_004_palindrome_product as mut

with such.A('Exercise 004 - Palindrome exercise') as it:
    @it.should('Calculate a 2x2 max palindrome correctly')
    def test_2_by_2():
        """ Test the 2x2 case """
        assert mut.find_palindrome_product(9, 99) == 9009
    @it.should('Solve the exercise correctly')
    def test_main():
        """ Check that it solves the main problem correctly """
        assert mut.run_main() == 906609


it.createTests(globals())

if __name__ == '__main__':
    nose2.main() # pragma: no cover
