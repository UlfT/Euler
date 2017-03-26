""" Nose2 test methods for tools/primes
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""
from math import sqrt
from itertools import islice, takewhile
import nose2
from nose2.tools import such
from src.tools import primes_helper


with such.A('My primes generator') as it:
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
    @it.should('Factorize a prime correctly')
    def test_factor_a_prime():
        """ Ensure that a prime is factored correctly """
        generate_10 = list(islice(primes_helper.primes(), 10))
        ans = primes_helper.get_factors(31, generate_10)[-1]
        assert ans == 31

it.createTests(globals())

if __name__ == '__main__':
    nose2.main() # pragma: no cover
