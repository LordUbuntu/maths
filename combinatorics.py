# Created by Jacobus Burger (2024)
# Info:
#   This file contains functions and constants for combinatorics


# Combinations
def C(n, k: int) -> int:
    return fact(n) // (fact(k) * fact(n - k))
