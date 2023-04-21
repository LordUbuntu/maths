# Jacobus Burger (2023)
# Info:
#   Calculus focused computing maths. Now with PI!
# Thanks:
#   Thanks to Professor Enriques Torres for teaching me Calculus 1 and
#   entertaining my interest in his research on Topological Homgroups.
#
#   Thanks so much to Professor Sam Pimentel for teaching me Calculus 2
#   and supporting me while I struggled and fell on my path to growth
#   in learning.
from math import sqrt, factorial, atan
from random import uniform


# various ways to calculate pi
class PI:
    # Srinivasa Ramanujan's pi estimate
    def ramanujan_pi(n = 0):
        sequence = 0
        for i in range(n + 1):
            sequence += (factorial(4*i) * (1103 + (26390 * i))) / (factorial(i)**4 * 396**(4*i))
        return (((2 * sqrt(2))/9801) * sequence) ** -1  # 1/pi -> pi


    # aproximate pi with some triangle magic
    def arc_pi():
        return atan(1) + atan(2) + atan(3)


    # sometimes pi can be approximated with a rational (fraction)
    def fractional_pi():
        return 22/7


    # calculate pi with John Machin formula (circ. 1706)
    def machin_pi():
        return 4 * (4 * atan(1/5) + atan(1/239))


    # calculate pi with Monte-Carlo method
    def monte_carlo_pi(n = 1000):
        circle, square = 0, 0
        for _ in range(n):
            if sqrt(uniform(-1, 1)**2 + uniform(-1, 1)**2) <= 1:
                circle += 1
            square += 1
        return (circle / square) * 4


    # Madhava-Leibniz Series
    def madhava_leibniz():
        return 4*atan(1)
