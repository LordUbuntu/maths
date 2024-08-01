# Jacobus Burger (2024-08-01)
# Desc:
#   I was trying to solve a problem with smoothing RPM data from my
#   tachometry code (tacho.py) while working on the Robotics Research
#   Project at TWU. I talked about the problem with Finian Lugtigheid
#   to see if there was a better way to do it than the average over a
#   dequeue. 
#   He proposed LERPing, and we figured out a way to adjust the alpha
#   value dynamically for situations where the wheels stops or changes
#   direction. This was perfect and I realized that it has many more
#   applications as well! Thanks Finian!
# Info:
#   https://en.wikipedia.org/wiki/Linear_interpolation
#   https://rachsmith.com/lerp/
# What:
#   Linear intERPolation of a polynomial function.
# Uses:
#   - Smoothing datapoints
#   - Computer Graphics
def lerp(x0: float, x1: float, alpha: float) -> float:
    return (1 - alpha) * x0 + alpha * x1
