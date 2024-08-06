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
from math import isfinite
import decimal
from hypothesis import given
from hypothesis.strategies import one_of, none, integers, floats, fractions, decimals



def clamp(value: int | float, minimum: int | float, maximum: int | float) -> int | float:
    if value is None or minimum is None or maximum is None:
        return float('nan')
    return max(minimum, min(value, maximum))





# Properties of clamp function:
# 0. clamp(a, b, c) == clamp(a, b, c)
#       for the same input, clamp must provide the same output
# 1. if min >= max, out == min
#       output is always at least lower bound
# 2. if min < max, min <= out <= max
#       output is bounded in interval [min, max]
# 3. if value, min, max == None, NaN, Infinity, etc, return NaN
#       undefined inputs return an undefined output
@given(
    value=one_of(none(), decimals(), floats(), fractions(), integers()),
    minimum=one_of(none(), decimals(), floats(), fractions(), integers()),
    maximum=one_of(none(), decimals(), floats(), fractions(), integers()),
)
def test_clamp(value: int | float, minimum: int | float, maximum: int | float) -> None:
    result = clamp(value, minimum, maximum)
    assert result == clamp(value, minimum, maximum)
    if minimum >= maximum:
        assert result == minimum
    elif minimum < maximum:
        assert minimum <= result <= maximum
