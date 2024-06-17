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


# Combinatorics on Words
# Prouhet-Thue-Morse sequence (parity sequence)
# https://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence
def PTM(length):
    bit = True
    for n in range(length):
        if ((n ^ (n - 1)).bit_length() + 1) & 1 == 0:
            bit = not bit
        yield int(bit)
