# Jacobus Burger (Created 2024-08-01, Last Updated 2025-04-27)
# Desc:
#   Clamping is a useful mathematical function when you want to ensure a
#   value remains fixed within a bound.
# Info:
#   https://en.wikipedia.org/wiki/Clamping_(graphics)
# What:
#   Limits values within a specified minimum and maximum value
# Uses:
#   - keeping values within an interval (inclusive)
from math import isfinite, isclose

import deal


# parameters are not None, NAN, or +/-Infinity
@deal.pre(
    lambda value, minimum, maximum: (value is not None and isfinite(value))
    and (minimum is not None and isfinite(minimum))
    and (maximum is not None and isfinite(maximum))
)
# return value will be between minimum and maximum
@deal.ensure(
    lambda value, minimum, maximum, result: min(minimum, maximum) <= result <= max(minimum, maximum) or isclose(result, minimum) or isclose(result, maximum)
)
# function is pure (no side-effects)
@deal.pure
def clamp(
    value: int | float, minimum: int | float, maximum: int | float
) -> int | float:
    """
    Bind value in inverval [minimum, maximum].

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
    Parameters cannot be None, NAN, or +/-Infinity.

    Postconditions
    --------------
    Return value will be between minimum and maximum.
    """
    # ensure minimum is minimum and maximum is maximum
    if maximum < minimum:
        minimum, maximum = maximum, minimum
    # return the value clamped between minimum and maximum
    return max(minimum, min(value, maximum))
