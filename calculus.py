# Jacobus Burger (2023)


# Srinivasa Ramanujan's pi estimate
from math import sqrt, factorial
def sr_pi(n = 0):
    sequence = 0
    for i in range(n + 1):
        sequence += (factorial(4*i) * (1103 + (26390 * i))) / (factorial(i)**4 * 396**(4*i))
    return ((2 * sqrt(2))/9801) * sequence
