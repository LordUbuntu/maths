# Jacobus Burger (Created 2018, Last Edited 2024-08-18)
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
#   Multiplication is one of the 6 common mathematical operations within
#   arithmetic. It gives you the product of repeating one value a by
#   a second value b amount of times. For example: "a times b" gives
#   you a many b's.
# Info:
#   https://en.wikipedia.org/wiki/Multiplication
from math import isfinite, nan, isnan
from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import one_of, integers, floats


# multiplication
# recursive multiplication
def multiplication_recursive(a: int | float, b: int | float):
    if a == 0:
        return b
    return multiplication_recursive(a - 1, b + a)


# iterative multiplication
def multiplication_iterative(a: int | float, b: int | float):
    # or with builtins just `return sum(itertools.repeat(b, a))`
    total = 0  # a _times_ b, a summed b times
    while a != 0:
        a -= 1
        total += b
    return total


multiplication = multiplication_iterative


# properties
#   https://en.wikipedia.org/wiki/Multiplication#Properties
# U. undefined returns undefined
# 0. zero property
# 1. identity
# 2. negation
# 3. commutativity
# 4. associativity
# 5. distributivity
# 6. inverse
# 7. order preservation
# 8. peano succession
MIN=-1_000_000
MAX=1_000_000
@given(
    a=one_of(
        integers(min_value=MIN, max_value=MAX),
        floats(min_value=MIN, max_value=MAX)
    ),
    b=one_of(
        integers(min_value=MIN, max_value=MAX),
        floats(min_value=MIN, max_value=MAX)
    ),
)
def test_multiplication(a: int | float, b: int | float):
    # U. undefined returns undefined
    if not isfinite(a) or not isfinite(b):
        assert isnan(multiplication(a, b))
        return
    # 0. zero property
    if a == 0 or b == 0:
        assert multiplication(a, b) == 0
    # 1. identity
    assert multiplication(a, 1) == a
    assert multiplication(b, 1) == b
    # 2. negation
    # TODO: just realizing that my implementation assumes positive numbers only...
    assert multiplication(a, -1) == -a
    assert multiplication(b, -1) == -b
    assert multiplication(-a, -1) == a
    assert multiplication(-b, -1) == b
    # 3. commutativity
    assert multiplication(a, b) == multiplication(b, a)
    # 4. associativity
    # TODO: not sure if this is right
    assert multiplication(multiplication(a, b), a) == multiplication(a, multiplication(a, b))
    # 5. distributivity
    # how would I do this?
    # 6. inverse
    assert multiplication(a, 1/a) == 1
    # 7. order preservation
    # 8. peano succession
    assert multiplication(a, 2) == a + a
