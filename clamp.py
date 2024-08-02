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
def clamp(value: int | float, minimum: int | float, maximum: int | float) -> int | float:
    return max(minimum, min(value, maximum))


# Property Based Testing:
# 1. middle: if min >= max, value == min
# 2. id: if all values are the same, they should return the value of value
# 3. min: if value is <= min, value == min
# 4. max: if value is >= max, value == max
# 5. interval: value must be in interval [min, max]

from hypothesis import given
from hypothesis.strategies import floats, integers

@given(integers(), integers(), integers())
def test_clamp_int(value: int, minimum: int, maximum: int):
    result = clamp(value, minimum, maximum)
    if minimum >= maximum:
        assert result == minimum
    elif minimum == maximum:
        assert result == minimum
        assert result == maximum
    elif value <= minimum:
        assert result == minimum
    elif value >= maximum:
        assert result == maximum
    else:
        assert minimum <= result
        assert result <= maximum
