# Jacobus Burger (2024)
# kaprekar's constant
# see:
#   https://en.wikipedia.org/wiki/6174
#   https://brilliant.org/wiki/kaprekars-constant/
KAPREKAR_CONSTANT = 6174


def count_steps(n, delay=0):
    from collections import deque
    from time import sleep
    """
    count_steps(n)

    counts the number of calculations between 'n' and the kaprekar constant
    """
    total_steps = 0
    while n != KAPREKAR_CONSTANT:
        # sort into increasing and decreasing numeric arrangement
        digits = [*str(n)]
        increasing = sorted(digits)
        decreasing = sorted(digits, reverse=True)
        # calculate next number in sequence
        n = int(''.join(decreasing)) - int(''.join(increasing))
        # count step
        total_steps = total_steps + 1 
        sleep(delay)
    return total_steps
