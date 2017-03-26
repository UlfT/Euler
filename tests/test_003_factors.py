""" Test code for ex_003_factors """

from math import sqrt
from itertools import islice, takewhile
from nose2.tools import such
import nose2
from src import ex_003_factors
with such.A('3rd exercise') as it:
    @it.should('Solve the task correctly')
    def test():
        """ Do the factorization given in the assignment"""
        assert ex_003_factors.run_main() == 6857

it.createTests(globals())

if __name__ == '__main__':
    nose2.main() # pragma: no cover
