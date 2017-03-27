""" Test code for ex_005_smallest_multiple """

from nose2.tools import such
from nose2.tools import params
import nose2
from src import ex_005_smallest_multiple as mut

with such.A('Exercise 005 - Smallest multiple') as it:
    @it.should('Solve the task correctly for known values')
    @params((10, 2520), (20, 232792560))
    def test(case, question, answer):
        """ Run parameterizes tests"""
        case.assert_(mut.find_smallest_multiple(question) == answer)

    @it.should('Run the main example without crashing')
    def test_main():
        """Just don't crash"""
        mut.run_main()

    @it.should('Throw exception if a faulty state is reached')
    def test_exception():
        """ Make the module fail"""
        try:
            mut.calculate_new_multiple(18, 2)
        except ValueError:
            assert True
        else:
            assert False


it.createTests(globals())

if __name__ == '__main__':
    nose2.main() # pragma: no cover
