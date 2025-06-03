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


# Permutation
# https://en.wikipedia.org/wiki/Permutation
def P(n, k):
    return factorial(n) // factorial(n - k)


# Combination / Binomial Coefficient
# https://en.wikipedia.org/wiki/Combination
def C(n, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))
    # or: return P(n, k) // P(k, k)


# Combinatorics on Words
# Prouhet-Thue-Morse sequence (parity sequence)
# https://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence
def PTM(length):
    bit = True
    for n in range(length):
        if ((n ^ (n - 1)).bit_length() + 1) & 1 == 0:
            bit = not bit
        yield int(bit)
