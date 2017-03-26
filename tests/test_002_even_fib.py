""" Tests for ex_002_even_fib"""
from itertools import takewhile
from nose2.tools import such
import nose2
from src import ex_002_even_fib as mut # mut = Module Under Test

with such.A('Fibonacci generator') as it:
    @it.should('Generate Fib numbers up to 90')
    def test_generator():
        """ Test the fibonacci generator"""
        less_than_90 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        generated = [fib_no for fib_no in takewhile(
            lambda x: x < 90, mut.fibonacci_generator())]
        assert less_than_90 == generated, \
            "Equals failed generated vs Hard coded {0}".format(generated)
    @it.should('Sum up all the even fib-numbers up to 90')
    def test_sum_of_even():
        """ Tests the sum_of_even_fibonacci_numbers method """
        # Even fib numbers below 90 are 2 8 34
        evensum = 2 + 8 + 34
        mutsum = mut.sum_of_even_fibonacci_numbers(90)
        assert evensum == mutsum, "Incorrect sum, expected {0} got {1}".format(evensum, mutsum)
    @it.should('Solve the actual Euler problem correctly')
    def test_main():
        """ Tests the main method, compares to the correct Euler answer 4613732"""
        answer = 4613732
        mut_answer = mut.run_main()
        assert answer == mut_answer, \
            "Main calculation incorrect,got {} expected {}".format(mut_answer, answer)

it.createTests(globals())

if __name__ == '__main__':
    nose2.main() # pragma: no cover
    