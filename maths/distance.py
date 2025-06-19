# Jacobus Burger (2025-06-18)
# Desc:
#   Mathematical functions for calculating distance.
# Info:
#   https://en.wikipedia.org/wiki/Euclidean_distance
#   https://en.wikipedia.org/wiki/Taxicab_geometry
#   https://en.wikipedia.org/wiki/Chebyshev_distance
# What:
#   Difference in position between two points.
# Uses:
#   - Finding the distance between two points.
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
    Calculate the Euclidean distance between two points p and q.

    Parameters
    ----------
    ps: tuple[int | float]
        Coordinate point of P represented as an n-tuple.
    qs: tuple[int | float]
        Coordinate point of Q represented as an n-tuple.

    Returns
    -------
    int | float
        Euclidean distance between P and Q.

    Preconditions
    -------------

    Postconditions
    --------------
    """
    pass


@deal.pure
def manhattan(
    ps: tuple[int | float], qs: tuple[int | float]
) -> int | float:
    """
    Calculate the manhattan distance between two points p and q.

    Parameters
    ----------
    ps: tuple[int | float]
        Coordinate point of P represented as an n-tuple.
    qs: tuple[int | float]
        Coordinate point of Q represented as an n-tuple.

    Returns
    -------
    int | float
        Manhattan distance between P and Q.

    Preconditions
    -------------

    Postconditions
    --------------
    """
    pass


@deal.pure
def chebyshev(
    ps: tuple[int | float], qs: tuple[int | float]
) -> int | float:
    """
    Calculate the Chebyshev distance between two points p and q.

    Parameters
    ----------
    ps: tuple[int | float]
        Coordinate point of P represented as an n-tuple.
    qs: tuple[int | float]
        Coordinate point of Q represented as an n-tuple.

    Returns
    -------
    int | float
        Chebyshev distance between P and Q.

    Preconditions
    -------------

    Postconditions
    --------------
    """
    pass


# function aliases
pythagorean = euclidean
taxicab = manhattan
chessboard = chebyshev
