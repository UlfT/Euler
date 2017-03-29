"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


Answer:
104743
"""
from src.tools import primes_helper

def get_prime_no(prime_no):
    """ Find prime numer prime_no"""
    primes = primes_helper.primes()
    for _ in range(1, prime_no):
        next(primes)
    return next(primes)

def run_main():
    """ Run the exercise as stated on the Euler website and wrapped in a timer"""
    from src.tools import timer_decorator
    wrapped_function = timer_decorator.wrap(get_prime_no)
    return wrapped_function(10001)

if __name__ == "__main__":
    run_main()  # pragma: no cover
