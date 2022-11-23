#!/bin/python3
# Created by Jacobus Burger (2018)
# Info:
#   A collection of various math-specific functions and programs
#   written for discrete mathematics to better understand concepts.
#   Everything herein was written for fun and practice.
#   I stand on the shoulders of giants, so I claim none of it as my own.
#
#   Thank you to Professor Richard J. Sutcliffe for being such an awesome
#   teacher and inspiration for both my discrete math courses.
#   I had a lot of fun taking that course (though it was hard) and hope to
#   carry this knowledge into my future, and continue to learn and improve
#   because of it. Hopefully I will grow and transform.
from functools import cache
from sys import maxsize as maxsize


# greatest common divisor
def gcd_iter(A, B):
    a = A
    b = B
    if b > a:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# least common multiple
def lcm_iter(A, B):
    big = A if A > B else B
    small = A if A < B else B
    for i in range(1, big + 2):
        for j in range(1, small + 2):
            a = big * i
            b = small * j
            if b == a:
                return b
            elif b > a:
                continue


# recursive implementation of gcd
@cache
def gcd(a, b):
    if b == 0:
        return a
    return rec_gcd(b, a % b)


# least common multiple
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# recursive max function
@cache
def max_rec(head: int, tail: list[int]) -> int:
    if len(tail) == 1:
        if head >= tail[0]:
            return head
        else:
            return tail[0]
    return max_rec(tail[0], tail[1:])


# recursive min function
@cache
def min_rec(head: int, tail: list[int]) -> int:
    if len(tail) == 1:
        if head < tail[0]:
            return head
        else:
            return tail[0]
    return min_rec(tail[0], tail[1:])


# iterative max function
def max_iter(nums: list[int]) -> int:
    max_val = -maxsize - 1
    for val in nums:
        if val > max_val:
            max_val = val
    return max_val


# iterative min function
def min_iter(nums: list[int]) -> int:
    min_val = maxsize
    for val in nums:
        if val < min_val:
            min_val = val
    return min_val


# show gcd reduction steps
def reduce(n, d):
    GCD = gcd(n, d)
    n = n / GCD
    d = d / GCD
    print("n: %i, d: %i, GCD: %i\n" % (n, d, GCD))


# factorial function
@cache
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


# binomial equation (combination)
def C(n, k):
    return fact(n) // (fact(k) * fact(n - k))


# permutation equation (permutation)
def P(n, k):
    return fact(n) // fact(n - k)


# euclidean division (modulo)
def mod(a, b):
    return a - b * (a // b)


# find the hamming distance of any two strings
def hamming_distance(a, b):
    if a == b:
        return 0
    return sum(map(lambda char: char[0] != char[1], zip(a, b)))


# maximal flow network backtracking algorithm
def max_flow():
    pass  # TODO
