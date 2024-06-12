# Created by Jacobus Burger (2024)
# Info:
#   This file contains functions and constants for combinatorics
from functools import cache


# factorial function
@cache
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Combinations
def C(n, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))


# Permutations
def P(n, k):
    return factorial(n) // factorial(n - k)
