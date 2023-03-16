# Jacobus Burger (2023)
# Calculus focues computing maths. Now with PI!
from math import sqrt, factorial


# Srinivasa Ramanujan's pi estimate
def ramanujan_pi(n = 0):
    sequence = 0
    for i in range(n + 1):
        sequence += (factorial(4*i) * (1103 + (26390 * i))) / (factorial(i)**4 * 396**(4*i))
    return ((2 * sqrt(2))/9801) * sequence


# aproximate pi with some triangle magic
def arc_pi():
    return atan(1) + atan(2) + atan(3)
