# Mathematical sieves to calculate primes using various methods



# Sieve of Eratosthenes
# In:  n, the sieve limit
# Out: sieve, the filter/mask to find primes with
from math import sqrt as sqrt
def soe(n: int):
    sieve = [True if i > 1 else False for i in range(n + 1)]
    # iterate through all integers from 2 to sqrt(n)
    for p in range(2, int(sqrt(n)) + 1):
        # skip any non-primes
        if sieve[p] == True:
            # eliminate all multiples i of current prime p, from p^2 to n.
            for i in range(p**2, n + 1, p):
                sieve[i] = False
    # you now have a sieve of primes
    return sieve
