""" Helper methods for all things primes related. The main algorithm is taken from
stackoverflow, but I will write it from memory to see that I have understood it.
Will try to keep this as methods and not as a class as long as possible"""

def primes():
    """ Infinite primes generator """
    current_value = 2
    witnesses = {}

    while True:
        if current_value not in witnesses:
            witnesses[current_value*current_value] = [current_value]
            yield current_value
        else:
            for witness in witnesses[current_value]:
                witnesses.setdefault(witness + current_value, []).append(witness)
            del witnesses[current_value]
        current_value += 1

def get_factors(number_to_factor, primes_list):
    """ Facorize number_to_factor return a list of the number if it was a prime"""
    remaining = number_to_factor
    factors = []
    for prime in primes_list:
        if remaining % prime == 0:
            factors.append(prime)
            while remaining % prime == 0:
                remaining /= prime
            if remaining == 1:
                return factors
    factors.append(number_to_factor) #The number is a prime
    return factors

def factor(to_factor):
    """ Helper method for the cases where you want to facor one single number """
    remaining = to_factor
    factors = []
    for prime in primes():
        if remaining % prime == 0:
            factors.append(prime)
            while remaining % prime == 0:
                remaining /= prime
            if remaining == 1:
                return factors
        if (prime * prime) > to_factor and factors == []:
            return [to_factor] # The input was a prime number
