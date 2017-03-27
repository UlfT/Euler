""" Nose2 test methods for tools/primes
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""
from math import sqrt
from itertools import islice, takewhile
import nose2
from nose2.tools import such
from nose2.tools import params
from src.tools import primes_helper


with such.A('Primes generator') as it:
    @it.should('Generate the first 10 primes correctly')
    def test_first10():
        """ Try to generate the first 10 primes"""
        first_10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        generate_10 = list(islice(primes_helper.primes(), 10))
        assert first_10 == generate_10, "Gave me {}".format(generate_10)

    @it.should('Get the correct prime factors for 13195')
    def test_simple_factors():
        """ Do the test factorization given in the assignment"""
        answer = [5, 7, 13, 29]
        maxno = int(sqrt(13195)) + 1
        primes_list = list(takewhile(lambda x: x <= maxno, primes_helper.primes()))
        assert answer == primes_helper.get_factors(13195, primes_list)
    @it.should('Factor a prime correctly using the two step model, asking for primes first')
    def test_factor_a_prime():
        """ Ensure that a prime is factored correctly """
        generate_10 = list(islice(primes_helper.primes(), 10))
        ans = primes_helper.get_factors(31, generate_10)[-1]
        assert ans == 31

    @it.should('Factor numbers correctly, using the automated model')
    @params([2,3], [3,5,11], [3,7], [257])
    def test_simple_factor(case, a_list):
        """ Ensure that a few numbers are correctly factored """
        to_check =  list_product(a_list)
        case.assert_ (primes_helper.factor(to_check) == a_list, "got {}, looking for {}".format(
            primes_helper.factor(to_check), a_list))

    def list_product(a_list):
        """ Helper function that multiplies all entries in a list """
        from functools import reduce
        return reduce(lambda x,y: x*y, a_list)

it.createTests(globals())

if __name__ == '__main__':
    nose2.main() # pragma: no cover
