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
from math import isfinite, sqrt
import deal


@deal.pre(lambda ps, qs: (ps is not None and ps != []) and (qs is not None and qs != []))
@deal.pre(lambda ps, qs: all(isfinite(p) for p in ps) and all(isfinite(q) for q in qs))
@deal.pure
def euclidean(
    ps: list[int | float], qs: list[int | float]
) -> int | float:
    """
    Calculate the Euclidean distance between two points p and q.

    Parameters
    ----------
    ps: list[int | float]
        Coordinate point of P.
    qs: list[int | float]
        Coordinate point of Q.

    Returns
    -------
    int | float
        Euclidean distance between P and Q.

    Preconditions
    -------------
    Inputs cannot be None, +/-Inf, Nan, or [].
    Both P and Q must be in the same dimensionaltiy or missing dimensions
        will be assumed to have a value of 0.

    Postconditions
    --------------
    """
    # correct missing dimensions
    if len(ps) < len(qs):
        ps.extend(0 for _ in range(len(qs) - len(ps)))
    if len(ps) > len(qs):
        qs.extend(0 for _ in range(len(ps) - len(qs)))
    # calculate euclidean / pythagorean distance
    #   for 1D
    if len(ps) == 1 and len(qs) == 1:
        return abs(ps[0] - qs[0])
    #   for nD
    return sqrt(sum((p - q) ** 2 for p, q in zip(ps, qs)))


@deal.pre(lambda ps, qs: (ps is not None and ps != []) and (qs is not None and qs != []))
@deal.pre(lambda ps, qs: all(isfinite(p) for p in ps) and all(isfinite(q) for q in qs))
@deal.pure
def manhattan(
    ps: list[int | float], qs: list[int | float]
) -> int | float:
    """
    Calculate the manhattan distance between two points p and q.

    Parameters
    ----------
    ps: list[int | float]
        Coordinate point of P.
    qs: list[int | float]
        Coordinate point of Q.

    Returns
    -------
    int | float
        Manhattan distance between P and Q.

    Preconditions
    -------------
    Inputs cannot be None, +/-Inf, Nan, or [].
    Both P and Q must be in the same dimensionaltiy or missing dimensions
        will be assumed to have a value of 0.

    Postconditions
    --------------
    """
    # correct missing dimensions
    if len(ps) < len(qs):
        ps.extend(0 for _ in range(len(qs) - len(ps)))
    if len(ps) > len(qs):
        qs.extend(0 for _ in range(len(ps) - len(qs)))
    # for 1D (note: same as euclidean)
    if len(ps) == 1 and len(qs) == 1:
        return abs(ps[0] - qs[0])
    # for nD
    return sum(abs(p - q) for p, q in zip(ps, qs))


@deal.pre(lambda ps, qs: (ps is not None and ps != ()) and (qs is not None and qs != ()))
@deal.pre(lambda ps, qs: all(isfinite(p) for p in ps) and all(isfinite(q) for q in qs))
@deal.pure
def chebyshev(
    ps: list[int | float], qs: list[int | float]
) -> int | float:
    """
    Calculate the Chebyshev distance between two points p and q.

    Parameters
    ----------
    ps: list[int | float]
        Coordinate point of P.
    qs: list[int | float]
        Coordinate point of Q.

    Returns
    -------
    int | float
        Chebyshev distance between P and Q.

    Preconditions
    -------------
    Inputs cannot be None, +/-Inf, Nan, or [].
    Both P and Q must be in the same dimensionaltiy or missing dimensions
        will be assumed to have a value of 0.

    Postconditions
    --------------
    """
    # correct missing dimensions
    if len(ps) < len(qs):
        ps.extend(0 for _ in range(len(qs) - len(ps)))
    if len(ps) > len(qs):
        qs.extend(0 for _ in range(len(ps) - len(qs)))
    # for 1D
    if len(ps) == 1 and len(qs) == 1:
        return abs(ps[0] - qs[0])  # by definition, max of just e is e
    # for nD
    return max(abs(p - q) for p, q in zip(ps, qs))


# function aliases
pythagorean = euclidean
taxicab = manhattan
chessboard = chebyshev
