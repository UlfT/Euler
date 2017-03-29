""" Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? """
from src.tools import primes_helper

def solve_exercise(num_to_solve):
    """ Find the largest factor of the number """
    return primes_helper.factor(num_to_solve)[-1]


def run_main():
    """ Run the exercise as stated on the Euler website and wrapped in a timer"""
    from src.tools import timer_decorator
    wrapped_function = timer_decorator.wrap(solve_exercise)
    return wrapped_function(600851475143)


if __name__ == "__main__":
    run_main() # pragma: no cover
