""" Exercise 2 of Project Euler
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms """
from itertools import takewhile


def fibonacci_generator():
    """ Return an endless generator of fibonnaci numbers
    Seed values are (1,1), so the next numbers in the sequence will be (1, 2, 3..)"""
    low, high = 1, 1
    while True:
        low, high = high, high + low
        yield low


def sum_of_even_fibonacci_numbers(upto):
    """ Sumarize all even fibonacci numbers up to, not including upto """
    upto_filter = lambda x: x < upto
    even_filter = lambda x: x % 2 == 0
    return sum(fib_no for fib_no in
               takewhile(upto_filter, fibonacci_generator()) if even_filter(fib_no))


def run_main():
    """ Run the exercise as stated on the Euler website and wrapped in a timer"""
    from src.tools import timer_decorator
    wrapped_function = timer_decorator.wrap(sum_of_even_fibonacci_numbers)
    return wrapped_function(4000000)

if __name__ == "__main__":
    run_main()  # pragma: no cover
