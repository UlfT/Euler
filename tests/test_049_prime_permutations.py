""" Test code for ex_049_prime_permutations """

from nose2.tools import such
import nose2
from src import ex_049_prime_permutations as mut

with such.A('Exercise 049 - Prime Permutations') as it:
    @it.should('Solve the main exercise')
    def test_main():
        """ Test the main method"""
        assert mut.run_main() == 296962999629

it.createTests(globals())

if __name__ == '__main__':
    nose2.main() # pragma: no cover
