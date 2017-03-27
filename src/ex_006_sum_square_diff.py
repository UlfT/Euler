""" 
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Mathing it, and looking at https://trans4mind.com/personal_development/mathematics/series/sumNaturalSquares.htm
sum of squares = (n)(n+1)(2n+1)/6
square of sums is square((n+1)*n/2)
"""

def solve(n):
    sum_of_squares = int((n)*(n+1)*(2*n+1)/6)
    square_of_sums = int((n * (n + 1) / 2) ** 2)
    return square_of_sums - sum_of_squares

def run_main():
    """ Run the exercise as stated on the Euler website and wrapped in a timer"""
    from src.tools import timer_decorator
    wrapped_function = timer_decorator.wrap(solve)
    return wrapped_function(100)

if __name__ == "__main__":
    run_main()  # pragma: no cover