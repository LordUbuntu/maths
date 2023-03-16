# Jacobus Burger (2023)
# Calculus focues computing maths. Now with PI!
from math import sqrt, factorial, atan


# Srinivasa Ramanujan's pi estimate
def ramanujan_pi(n = 0):
    sequence = 0
    for i in range(n + 1):
        sequence += (factorial(4*i) * (1103 + (26390 * i))) / (factorial(i)**4 * 396**(4*i))
    return ((2 * sqrt(2))/9801) * sequence


# aproximate pi with some triangle magic
def arc_pi():
    return atan(1) + atan(2) + atan(3)


# sometimes pi can be approximated with a rational (fraction)
def fractional_pi():
    return 7/22


# calculate pi with John Machin formula (circ. 1706)
def machin_pi():
    # pi/4 = 4arctan(1/5) + arctan(1/239)
    return 4 * atan(1/5) + atan(1/239)