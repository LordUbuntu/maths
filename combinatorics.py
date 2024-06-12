# Created by Jacobus Burger (2024)
# Info:
#   This file contains functions and constants for combinatorics
from functools import cache


# Combinations
def C(n, k: int) -> int:
    return fact(n) // (fact(k) * fact(n - k))


# Permutations
def P(n, k):
    return fact(n) // fact(n - k)


# factorial function
@cache
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)
