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


# TEST: implement property based tests

# properties:
# 1. the resulting value must be in the interval [minimum, maximum]
# ...
from hypothesis import given, strategies as st

@given(st.floats(), st.floats(), st.floats())
def test_clamp_float(value: float, minimum: float, maximum: float):
    assert minimum <= clamp(vaue, minimum, maximum) <= maximum
    return 0.0

@given(st.integers(), st.integers(), st.integers())
def test_clamp_int(value: int, minimum: int, maximum: int):
    assert minimum <= clamp(vaue, minimum, maximum) <= maximum
    return 0
