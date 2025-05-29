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
import clamp  # avoid rewrite by using clamp
from math import isfinite
import deal


@deal.pre(lambda a, b, alpha: isfinite(a) and isfinite(b) and isfinite(alpha))
@deal.pre(lambda a, b, alpha: (a is not None) and (b is not None) and (alpha is not None))
@deal.ensure(lambda a, b, alpha, result: a <= result <= b)
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
