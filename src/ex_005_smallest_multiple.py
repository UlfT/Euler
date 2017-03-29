""""" Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
from operator import mul
from functools import reduce

def smallest_multiple(upto):
    multiples=[]
    for num in range(upto, 1, -1):
        for multiple in multiples:
            if multiple % num == 0:
                break
        else:
            multiples.append(num)
    print(multiples)
    return reduce(mul, multiples, 1)
                
                
if __name__ == '__main__':
    print(smallest_multiple(10))