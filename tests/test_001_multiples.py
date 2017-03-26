""" Tests for ex_001_multiples"""
from nose2.tools import such
import nose2 # pragma: no cover
from src import ex_001_multiples as mut # mut = Module Under Test


with such.A('Silly multiples module') as it:
    @it.should('Correctly check if a number is a multiple of 3 or 5')
    def test_is_multiple():
        """ Tests the is_multiple_of_3_or_5 method"""
        assert mut.is_multiple_of_3_or_5(3), "Expected to see that 3 was an multiple"
        assert mut.is_multiple_of_3_or_5(5), "Expected to see that 5 was an multiple"
        assert mut.is_multiple_of_3_or_5(3*3*5*5),\
                        "Expected to see that 9x25 was an multiple"
        assert not(mut.is_multiple_of_3_or_5(7)), "7 should not be a multiple"

    @it.should('correctly sum up multiples of 3 and 5')
    def test_sum():
        """ Tests the sum_of_3_5_multiples method. Only tests for positive numbers"""
        assert mut.sum_of_3_5_multiples(10) == 23, "Textbook example of 10 and 23 failed"

    @it.should('solve the Euler problem correctly')
    def test_exercise():
        """ TODO: Add a timer that fires if the calculation takes more than 1 second
            But that does not work on Windows so screw it """
        assert mut.run_main() == 233168, "Correct answer should be 233168"

it.createTests(globals())

if __name__ == '__main__':
    nose2.main() # pragma: no cover
