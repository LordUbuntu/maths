# Jacobus Burger (2023)
# An implementation of the Collatz Algorithm
from collections.abc import Generator


def collatz_generator(n: int) -> Generator[int]:
    """
    Generate a sequence for the collatz conjecture starting at n.

    Parameters
    ----------
    n : int | float
        Starting value of collatz conjecture.

    Returns
    -------
    Generator[int]
        Each step yields the nth value of the sequence.
    """
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else n * 3 + 1


def collatz(n: int) -> int:
    """Calculate steps for collatz conjecture."""
    step = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else n * 3 + 1
        step += 1
    return step


# One obvious pattern to observe: when we hit _any_ power of 2, the sequence
#   becomes linear and will complete from that point in log2 of n steps. How
#   to predict the point where the collatz conjecture will land on this path
#   thought, that doesn't seem so obvious.
