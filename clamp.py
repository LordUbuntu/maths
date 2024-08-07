# Jacobus Burger (2024-08-01)
# Desc:
#   Clamping is a useful mathematical function when you want to ensure a
#   value remains fixed within a bound.
# Info:
#   https://en.wikipedia.org/wiki/Clamping_(graphics)
# What:
#   Limits values within a specified minimum and maximum value
# Uses:
#   - keeping values within an interval (inclusive)
from math import isfinite, nan, isnan
from hypothesis import given
from hypothesis.strategies import one_of, none, integers, floats, fractions, decimals


# clamp function
# clamp: [a, b, c] -> R, if forall b in R, a <= f(b) <= c
def clamp(value: int | float, minimum: int | float, maximum: int | float) -> int | float:
    # return nan for undefined inputs
    if value is None or minimum is None or maximum is None:
        return nan
    if not isfinite(value) or not isfinite(minimum) or not isfinite(maximum):
        return nan
    # return clamp of function otherwise
    return max(minimum, min(value, maximum))


# Properties of clamp function:
# 0. if value, min, max == undefined, return nan
#       undefined inputs return an undefined output (nan)
# 1. clamp(a, b, c) == clamp(a, b, c)
#       for the same input, clamp must provide the same output
# 2. if min >= max, out == min
#       output is always at least lower bound
# 3. if min < max, min <= out <= max
#       output is bounded in interval [min, max]
@given(
    value=one_of(none(), floats(), fractions(), integers()),
    minimum=one_of(none(), floats(), fractions(), integers()),
    maximum=one_of(none(), floats(), fractions(), integers()),
)
def test_clamp(value: int | float, minimum: int | float, maximum: int | float) -> None:
    # 0
    if value is None or minimum is None or maximum is None:
        assert isnan(clamp(value, minimum, maximum))
        return
    if not isfinite(value) or not isfinite(minimum) or not isfinite(maximum):
        assert isnan(clamp(value, minimum, maximum))
        return
    # 1
    result = clamp(value, minimum, maximum)
    assert result == clamp(value, minimum, maximum)
    # 2
    if minimum >= maximum:
        assert result == minimum
    # 3
    elif minimum < maximum:
        assert minimum <= result <= maximum
