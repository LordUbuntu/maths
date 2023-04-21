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
    def ramanujan_pi_series(self, n = 0):
        sequence = 0
        for i in range(n + 1):
            sequence += (factorial(4*i) * (1103 + (26390 * i))) / (factorial(i)**4 * 396**(4*i))
        return (((2 * sqrt(2))/9801) * sequence) ** -1  # 1/pi -> pi


    # aproximate pi with some triangle magic
    def arc_pi(self):
        return atan(1) + atan(2) + atan(3)


    # sometimes pi can be approximated with a rational (fraction)
    def fractional_pi(self):
        return 22/7


    # calculate pi with John Machin formula (circ. 1706)
    def machin_pi(self):
        return 4 * (4 * atan(1/5) + atan(1/239))


    # calculate pi with Monte-Carlo method
    def monte_carlo_pi(self, n = 1000):
        circle, square = 0, 0
        for _ in range(n):
            if sqrt(uniform(-1, 1)**2 + uniform(-1, 1)**2) <= 1:
                circle += 1
            square += 1
        return (circle / square) * 4


    # Madhava-Leibniz method (π = 4arctan(1))
    def madhava_leibniz_pi(self):
        return 4 * atan(1)

    # Madhava-Leibniz Series
    def madhava_leibniz_pi_series(self, terms = 7):
        # 1 - 1/3 + 1/5 - 1/7...
        total = 0
        for n in range(1, terms + 1):
            total += ((-1)**(n-1)) * (1 / (2*n - 1))
        return total
