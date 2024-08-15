# Jacobus Burger (Created 2018, Last Edited 2024-08-08)
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
#   Fibbonacci sequence is an interesting mathematical sequence of numbers
#   where each successive number is the sum of the previous two. It has
#   interesting properties like approximating the golden ratio.
# Info:
#   https://en.wikipedia.org/wiki/Fibonacci_sequence
from functools import cache
from hypothesis import given
from hypothesis.strategies import integers


# fibbonacci sequence (recursive)
@cache
def fib_recursive(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# fibbonacci sequence (iterative)
def fib_iterative(n: int) -> int:
    a, b = 1, 1
    for i in range(n):
        a, b = a + b, a
    return a
