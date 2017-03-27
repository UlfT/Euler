""" Test code for ex_007_10001st_prime """

from nose2.tools import such
from nose2.tools import params
import nose2
from src import ex_007_10001st_prime as mut

with such.A('Exercise 007 - Prime counting') as it:
    @it.should('Solve the main exercise')
    def test_main():
        assert mut.run_main() == 104743

it.createTests(globals())

if __name__ == '__main__':
    nose2.main() # pragma: no cover