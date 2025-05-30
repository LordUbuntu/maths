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
#   Modulo is one of the two types of division in Euclidean Division
#   which determines the remainder of a division. So for example
#   3 % 2 == 1 since there's a remainder of one. It's used a lot in
#   all sorts of mathematics, it's most helpful in determining
#   divisibility (like n % 2 == 0 indicated a number is even).
# Info:
#   https://en.wikipedia.org/wiki/Modulo
import math


# euclidean division (modulo)
# a = bq + r, => r = a - bq
def mod(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return math.nan
    return a - (b * (a // b))


# properties
# 0. zero - n mod 0 == undefined
# 1. identity - n mod n == 0
from hypothesis import given
from hypothesis.strategies import integers


@given(a=integers(), b=integers())
def test_mod(a: int, b: int):
    # 0
    if a == 0 or b == 0:
        assert math.isnan(mod(a, b))
    # 1
    assert mod(a, a) == 0
    assert mod(b, b) == 0
