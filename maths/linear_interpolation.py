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
from math import isfinite, isnan, nan

import clamp  # avoid rewrite by using clamp
import deal


@deal.pre(lambda a, b, alpha: isfinite(a) and isfinite(b) and isfinite(alpha))
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
        Interpolated value between a and b


    Preconditions
    -------------
    Inputs must be defined (not None, NAN, or +/-Infinity).
    a must be less than or equal to b.
    alpha must be between (inclusive) 0.0 and 1.0.

    Postconditions
    --------------
    Output will be between a and b (inclusive).
    """
    if b < a:
        a, b = b, a
    alpha = clamp.clamp(alpha, 0.0, 1.0)
    return (1 - alpha) * a + alpha * b
