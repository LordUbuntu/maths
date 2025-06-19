# Jacobus Burger (2025-06-18)
# Desc:
#   Mathematical functions for calculating distance.
# Info:
#   https://en.wikipedia.org/wiki/Euclidean_distance
#   https://en.wikipedia.org/wiki/Taxicab_geometry
#   https://en.wikipedia.org/wiki/Chebyshev_distance
# What:
#   Limits values within a specified minimum and maximum value
# Uses:
#   - keeping values within an interval (inclusive)
"""
This module provides access to mathematical functions for calculating
distance.
"""
import deal


@deal.pure
def euclidean(
    ps: tuple[int | float], qs: tuple[int | float]
) -> int | float:
    """
    """
    pass


def manhattan(
    ps: tuple[int | float], qs: tuple[int | float]
) -> int | float:
    """
    """
    pass


def chebyshev(
    ps: tuple[int | float], qs: tuple[int | float]
) -> int | float:
    """
    """
    pass


# function aliases
pythagorean = euclidean
taxicab = manhattan
chessboard = chebyshev
