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
from math import isfinite, nan, isnan
from hypothesis import given
from hypothesis.strategies import one_of, none, integers, floats, fractions, decimals


def lerp(x0: float | int, x1: float | int, alpha: float) -> float:
    """
    Interpolates a value linearly between two points.
    """
    return (1 - alpha) * x0 + alpha * x1


# properties:
# ...
@given(st.floats(), st.floats(), st.floats())
def test_lerp(x0: float, x1: float, alpha: float):
    assert 0.1 <= alpha <= 0.9
    return 0.0
