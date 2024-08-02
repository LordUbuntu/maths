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


# properties:
# 1. id: if all values are the same, they should return the value of value
# 2. min: if value is <= min, value == min
# 3. max: if value is >= max, value == max
# 4. middle: if min >= max, value == min
# 5. interval: value must be in interval [min, max]

from hypothesis import given
from hypothesis.strategies import floats, integers

@given(floats(), floats(), floats())
def test_clamp_float(value: float, minimum: float, maximum: float):
    result = clamp(value, minimum, maximum)
    if value == minimum and value == maximum:
        assert result == minimum
        assert result == maximum
    if value <= minimum:
        assert result == minimum
    if value >= maximum:
        assert result == maximum
    if minimum >= maximum:
        assert result == minimum
    assert minimum <= result <= maximum

@given(integers(), integers(), integers())
def test_clamp_int(value: int, minimum: int, maximum: int):
    assert minimum <= clamp(value, minimum, maximum) <= maximum
    return 0
