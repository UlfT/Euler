""" Exercise 1 of Project Euler
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""


def is_multiple_of_3_or_5(to_test):
    """ Test if to_test is a multiple of 3 or 5.
    returns a boolean"""
    return (to_test % 3 == 0) or (to_test % 5 == 0)


def sum_of_3_5_multiples(upto):
    """ Returns the sum of all integers that are multiples of 3 or 5"""
    my_sum = 0
    for counter in range(1, upto):
        if is_multiple_of_3_or_5(counter):
            my_sum += counter
    return my_sum


def run_main():
    """ Run the exercise as stated on the Euler website and wrapped in a timer"""
    from src.tools import timer_decorator
    wrapped_function = timer_decorator.wrap(sum_of_3_5_multiples)
    return wrapped_function(1000)

if __name__ == "__main__":
    run_main()  # pragma: no cover
