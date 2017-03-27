"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

The algorithm is as follows:
- Start by multiplying all the primes in the interval together. What ever the answer is, it will be a multiple of that. 
- Since we go from low to high, then for a non-prime number x the result will either already be divisable by x,
 or it will be if we muliply by _one_ of the prime factors of x. 
"""
from src.tools import primes_helper

def find_smallest_multiple(upto_num):
    primes = primes_helper.factor(upto_num)
    res = list_product(primes_helper.factor(upto_num))
    for a_num in range(2, upto_num + 1):
        if res % a_num != 0: # res divides all the primes, and some others
            res = calculate_new_multiple(a_num, res)
    return res

def calculate_new_multiple(a_num, res):
    factors = primes_helper.factor(a_num)
    for attempt in factors:
        if (res* attempt) % a_num == 0:
            return res* attempt
    raise Exception("Incorrect program state!") # pragma: no cover

def list_product(a_list):
    """ Helper function that multiplies all entries in a list """
    from functools import reduce
    return reduce(lambda x,y: x*y, a_list)

def run_main():
    """ Run the exercise as stated on the Euler website and wrapped in a timer"""
    from src.tools import timer_decorator
    wrapped_function = timer_decorator.wrap(find_smallest_multiple)
    return wrapped_function(20)

if __name__ == "__main__":
    run_main()  # pragma: no cover