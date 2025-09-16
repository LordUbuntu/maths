# Jacobus Burger (Created 2018, Last Edited 2024-08-08)
# Prologue:
#   This was sourced from discrete.py which was originally written in
#   2018/2022 to better understand and learn discrete math. That was
#   done for fun and practice, and inspired by the great influence of
#   my discrete math Professors Richard J Sutcliffe.
#
#   Thank you to Professor Richard J. Sutcliffe for being such an awesome
#   teacher and inspiration in both my discrete math courses.
#   I had a lot of fun taking those courses (though it was hard) and
#   I hope to carry the knowledge into my future, and continue to learn
#   and improve because of it. I will grow and transform.
# Desc:
#   Hamming Distance calculates the distance / amount of difference
#   between two strings of information (usually binary numbers, but
#   can be for any sequential pieces of data, aka: strings/vectors).
# Info:
#   https://en.wikipedia.org/wiki/Hamming_distance
from itertools import zip_longest
from operator import ne

import deal

T = str | list[int | float | str]


# find the hamming distance of any two strings
# this should work with lists, strings, and other sequential data types
#
# I need to rework input type for hamming distance tests before this
#   precondition can be met
# @deal.pre(lambda a, b: len(a) == len(b))
# @deal.pre(lambda a, b: type(a) is type(b))
@deal.post(lambda result: type(result) is int and result >= 0)
@deal.pure
def hamming_distance(a: T, b: T) -> int:
    """
    Calculate the hamming distance between two sequences of same type.

    Parameters
    ----------
    a : list | tuple | str
        First sequence to compare with.
    b : list | tuple | str
        Second sequence to compare with.

    Returns
    -------
    int
        The difference between the two sequences.

    Preconditions
    -------------
    Input parameters must be of the same type and length.

    Postconditions
    --------------
    Output parameter must be of type int and greater than 0.
    """
    # plan: zip longest, compare elements, adding sum of comparison?
    return sum(map(lambda t: ne(t[0], t[1]), zip_longest(a, b)))
