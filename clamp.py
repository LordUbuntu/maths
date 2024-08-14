# Jacobus Burger (Created 2024-08-01, Last Updated 2024-08-07)
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
from hypothesis.strategies import one_of, none, integers, floats


def clamp(value: int | float, minimum: int | float, maximum: int | float) -> int | float:
    """
    Binds value between (and including) a minimum and maximum bound.

    Parameters
    ----------
    value : int | float
        Input to be bounded.
    minimum : int | float
        Lower bound for Output.
    maximum : int | float
        Upper bound for Output.

    Returns
    -------
    int | float
        Bounded Output number.

    Preconditions
    -------------
    Parameters cannot be None, NAN, or +/-Infinity

    Postconditions
    --------------
    Output will not be < minimum
    Output will not be > maximum
    """
    # return nan for undefined inputs
    if not isfinite(value) or not isfinite(minimum) or not isfinite(maximum):
        return nan
    # return clamp of function otherwise
    return max(minimum, min(value, maximum))


# Properties of clamp function:
# 0. if value, min, max == undefined, return nan
#       undefined inputs return an undefined output (nan)
#
# 1. clamp(a, b, c) == clamp(a, b, c)
#       for the same input, clamp must provide the same output
# 2. oracle answer == clamp(a, b, c)
@given(
    value=one_of(integers(), floats()),
    minimum=one_of(integers(), floats()),
    maximum=one_of(integers(), floats()),
)
def test_clamp(value: int | float, minimum: int | float, maximum: int | float) -> None:
    # 0. undefined inputs return an undefined output (nan)
    if not isfinite(value) or not isfinite(minimum) or not isfinite(maximum):
        assert isnan(clamp(value, minimum, maximum))
        return
    # 1. for the same input, clamp must provide the same output
    assert clamp(value, minimum, maximum) == clamp(value, minimum, maximum)
    # 2. oracle answer == clamp(a, b, c)
    answer = value
    if answer < minimum:
        answer = minimum
    elif answer > maximum:
        answer = maximum
    else:
        answer = value
    assert clamp(value, minimum, maximum) == answer
