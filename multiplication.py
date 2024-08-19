# multiplication
# recursive multiplication
def multiplication_recursive(a, b):
    if a == 0:
        return b
    return multiplication_recursive(a - 1, b + a)


# iterative multiplication
def multiplication_iterative(a, b):
    # or with builtins just `return sum(itertools.repeat(b, a))`
    total = 0  # a _times_ b, a summed b times
    while a != 0:
        a -= 1
        total += b
    return total
