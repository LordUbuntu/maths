# Jacobus Burger (2022)
# Sieve of Eratosthenes in Python
# see: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
from math import sqrt as sqrt


def sieve(n: int) -> list[bool]:
    # initialize all except 0 and 1 to True
    primes = [True if i > 1 else False for i in range(n + 1)]
    # iterate through all integers from 2 to sqrt(n)
    for p in range(2, int(sqrt(n)) + 1):
        # skip any non-primes
        if primes[p]:
            # eliminate all multiples i of current prime p, from p^2 to n
            for i in range(p**2, n + 1, p):
                primes[i] = False
    # you now have the sieve of eratosthenes
    return primes
