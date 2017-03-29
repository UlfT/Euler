""""" Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
For 2x2 -> the palindrome can be written abba.
1000 a + 1a = 1001a
100b + 10b = 110b
Simplify to
11x(91a + 10b)

for 3x3 the math becomes (abccba)
100001a + 10010b + 1100c
11x (9091z, 910b, 100c)
"""

def find_palindrome_product(from_number, to_number):
    """ "Find the largest palindrome number"""
    largest_product = 0
    # Ensure that the to_number is divisible by 11 according to above math
    modified_to = 11 * int((to_number / 11))
    for smallstep in range(to_number, from_number, -1):
        for bigstep in range(modified_to, from_number, -11):
            prod = bigstep * smallstep
            if prod <= largest_product:
                break
            if is_palindrome(str(prod)):
                largest_product = prod

    return largest_product

def is_palindrome(to_check):
    """ Check if a string is a palindrome"""
    return to_check == to_check[::-1]

def run_main():
    """ Run the exercise as stated on the Euler website and wrapped in a timer"""
    from src.tools import timer_decorator
    wrapped_function = timer_decorator.wrap(find_palindrome_product)
    return wrapped_function(99, 999)

if __name__ == "__main__":
    run_main() # pragma: no cover
