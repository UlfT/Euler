""" Test code for ex_006_sum_square_diff """

from nose2.tools import such
from nose2.tools import params
import nose2
from src import ex_006_sum_square_diff as mut

with such.A('Sum square exercise') as it:
    @it.should('Solve the main exercise')
    def test_main():
        assert mut.run_main() == 25164150

it.createTests(globals())

if __name__ == '__main__':
    nose2.main() # pragma: no cover