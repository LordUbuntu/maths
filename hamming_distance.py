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
import operator as op
from typing import Sequence, TypeVar
T = TypeVar('T', Sequence[int], Sequence[float], str)
from hypothesis.strategies import one_of, none, lists, integers, floats, fractions, decimals


# find the hamming distance of any two strings
# this should work with lists, strings, and other sequential data types
def hamming_distance(a: T, b: T) -> int:
    return sum(map(op.ne, a, b))



# properties
# 0. undefined values
# 1. mismatching lengths truncate longer list and count extra length to hamming distance
# 2. the same input for both a and b should give 0
# TODO:
# - read whole series to understand property based testing better
# - https://fsharpforfunandprofit.com/posts/property-based-testing-2/
@given(
    a=one_of(none(), lists(integers()), lists(floats()))
    b=one_of(none(), lists(integers()), lists(floats()))
)
def test_hamming_distance(a: T, b: T):
    pass
