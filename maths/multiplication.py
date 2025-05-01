# Jacobus Burger (Created 2018, Last Edited 2024-08-18)
# Prologue:
#   This was sourced from discrete.py which was originally written in
#   2018/2022 to better understand and learn discrete math. That was
#   done for fun and practice, and inspired by the great influence of
#   my discrete math Professors Richard J Sutcliffe.
#
#   Thank you to Professor Richard J. Sutcliffe for being such an awesome
#   teacher and inspiration in both my discrete math courses.
#   I had a lot of fun taking those courses (though it was hard) and
#   I hope to carry the knowledge into my future, and continue to learn
#   and improve because of it. I will grow and transform.
# Desc:
#   Multiplication is one of the 6 common mathematical operations within
#   arithmetic. It gives you the product of repeating one value a by
#   a second value b amount of times. For example: "a times b" gives
#   you a many b's.
# Info:
#   https://en.wikipedia.org/wiki/Multiplication
#   https://en.wikipedia.org/wiki/Multiplication_algorithm
from math import isfinite
import deal


# multiplication
# recursive multiplication
@deal.pre(lambda a, b: (a is not None and isfinite(a)) and (b is not None and isfinite(b)))
@deal.ensure(lambda a, b, result: result == a * b)
@deal.pure
def multiplication_recursive(a: int | float, b: int | float):
    if a == 0:
        return b
    return multiplication_recursive(a - 1, b + a)


# iterative multiplication
def multiplication_iterative(a: int | float, b: int | float):
    # or with builtins just `return sum(itertools.repeat(b, a))`
    total = 0  # a _times_ b, a summed b times
    while a != 0:
        a -= 1
        total += b
    return total

# the iterative and recursive implementations are effectively the
#   same thing. I think this is an example of the
#   curry-howard isomorphism?
