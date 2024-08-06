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
import typing

def clamp(value: int | float, minimum: int | float, maximum: int | float) -> int | float:
    return max(minimum, min(value, maximum))





# Properties of clamp function:
# 0. clamp(a, b, c) == clamp(a, b, c)
#       for the same input, clamp must provide the same output
# 1. if min >= max, out == min
#       output is always at least lower bound
# 2. if min < max, min <= out <= max
#       output is bounded in interval [min, max]
import decimal
import fractions
from hypothesis import given
from hypothesis.strategies import one_of, integers, floats, fractions, decimals


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
