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
import math
import operator as op
from typing import List, TypeVar
T = TypeVar('T', List[int], List[float], str)
from hypothesis import given
from hypothesis.strategies import one_of, none, lists, integers, floats, fractions, decimals


# find the hamming distance of any two strings
# this should work with lists, strings, and other sequential data types
def hamming_distance(a: T, b: T) -> int:
    # satisfy preconditions
    if a is None and b is None:
        return 0
    if a is None and b is not None:
        return len(b)
    if a is not None and b is None:
        return len(a)
    # haming distance + difference of lengths
    return sum(map(op.ne, a, b)) + abs(len(a) - len(b))



# properties
# 0. if either undefined, return other's length
# 1. if both undefined, return nan
# 2. identity: if a == b, hamming_distance(a, b) == 0
# 3. idempotence: doing the same operation twice should yield the same output
# 4. mismatching lengths truncate longer list and count extra length to hamming distance
# TODO:
# - read whole series to understand property based testing better
# - https://fsharpforfunandprofit.com/posts/property-based-testing-2/
@given(
    a=one_of(none(), lists(integers()), lists(floats())),
    b=one_of(none(), lists(integers()), lists(floats())),
)
def test_hamming_distance(a: T, b: T):
    # 0. if either undefined, return other's length
    if a is None or b is None:
        assert math.isnan(hamming_distance(a=a, b=b))
        return
    if not math.isfinite(a) or not math.isfinite(b):
        assert math.isnan(hamming_distance(a=a, b=b))
        return
    # 1. identity
    if a == b:
        assert hamming_distance(a, b) == 0
    # 2. idempotence
    assert hamming_distance(a, a) == hamming_distance(a, a)
    assert hamming_distance(b, b) == hamming_distance(b, b)
    assert hamming_distance(a, b) == hamming_distance(a, b)
    assert hamming_distance(b, a) == hamming_distance(b, a)
    # 3. mismatch length should return total of hamming and length diff
    if len(a) != len(b):
        if len(a) > len(b):
            length_diff = len(a) - len(b)
            hamming = 0
            for i in range(len(b)):
                if a[i] != b[i]:
                    hamming += 1
            assert hamming + length_diff == hamming_distance(a, b)
        else:
            expected = len(b) - len(a)
            hamming = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    hamming += 1
            assert hamming + length_diff == hamming_distance(a, b)
