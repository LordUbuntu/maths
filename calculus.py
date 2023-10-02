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
from math import sqrt, factorial, atan, asin
from random import uniform


class Series:
    def __init__(self, function, start, end):
        self.function = function
        self.start = start
        self.end = end


# generalized sequence
def sequence(function, start, end):
    for n in range(start, end):
        yield function(n)


# generalized series
def series(function, start, end):
    return sum(sequence(function, start, end))


# various ways to calculate pi
class PI:
    # Srinivasa Ramanujan's π estimate
    def ramanujan_pi_series(self, n = 0):
        sequence = 0
        for i in range(n + 1):
            sequence += (factorial(4*i) * (1103 + (26390 * i))) / (factorial(i)**4 * 396**(4*i))
        return (((2 * sqrt(2))/9801) * sequence) ** -1  # 1/pi -> pi


    # aproximate π with some triangle magic
    def arc_pi(self):
        return atan(1) + atan(2) + atan(3)


    # sometimes π can be approximated with a rational (fraction)
    def fractional_pi(self):
        return 22/7


    # calculate π with John Machin formula (circ. 1706)
    def machin_pi(self):
        return 4 * (4 * atan(1/5) + atan(1/239))


    # calculate π with Monte-Carlo method
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


    # Madhava-Leibniz Series π
    def madhava_leibniz_pi_series(self, terms = 7):
        # 1 - 1/3 + 1/5 - 1/7...
        total = 0
        for n in range(1, terms + 1):
            total += ((-1)**(n-1)) * (1 / (2*n - 1))
        return 4 * total


    # greek bound of pi from triangles...
    def greek_bound_pi(self):
        return "3 < 𝛑 < 4"


    def arcsin_pi(self):
        return asin(1) * 2  # arcsin(1) = pi/2
