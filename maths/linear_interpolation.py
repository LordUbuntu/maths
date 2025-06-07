# Jacobus Burger (Created 2024-08-01, Last Updated 2024-08-07)
# Desc:
#   I was trying to solve a problem with smoothing RPM data from my
#   tachometry code (tacho.py) while working on the Robotics Research
#   Project at TWU. I talked about the problem with Finian Lugtigheid
#   to see if there was a better way to do it than the average over a
#   dequeue.
#   He proposed LERPing which was a perfect fit to smooth the tachometry
#   data and many other things too! Thanks Finian!
# Info:
#   https://en.wikipedia.org/wiki/Linear_interpolation
#   https://rachsmith.com/lerp/
# What:
#   Linear intERPolation of a polynomial function.
# Uses:
#   - Smoothing datapoints
#   - Computer Graphics
from math import isfinite, isclose

import deal


@deal.pre(lambda a, b, alpha: isfinite(a) and isfinite(b) and isfinite(alpha))
@deal.pre(
    lambda a, b, alpha: (a is not None)
    and (b is not None)
    and (alpha is not None)
)
@deal.ensure(
    lambda a, b, alpha, result: min(a, b) <= result <= max(a, b)
    or isclose(result, a)
    or isclose(result, b)
)
@deal.pure
def lerp(a: int | float, b: int | float, alpha: float) -> float:
    """
    Interpolates a value linearly between two points.

    Parameters
    ----------
    a : int | float
        previous value.
    b : int | float
        current value.
    alpha : float
        interpolation ratio (higher prefers b, lower prefers a).

    Returns
    -------
    float
        Interpolated value between a and b.


    Preconditions
    -------------
    Inputs must be defined (not None, NAN, or +/-Infinity).

    Postconditions
    --------------
    Output will be between a and b (inclusive).
    """
    alpha = 0.0 if alpha < 0 else alpha
    alpha = 1.0 if alpha > 1 else alpha
    return (1 - alpha) * a + alpha * b

# floating point precision comes to haunt in situations (for example)
# where result=9089709072426400.0, a=0.0, b=9089709072426399, alpha=1.0
# so a workaround is to use Decimal to represent floating numbers exactly
