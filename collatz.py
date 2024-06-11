# Jacobus Burger (2023)
# An implementation of the Collatz Algorithm


def flatten(generator):
    """
    Flatten a generator into a list
    """
    return [*generator]


def collatz_generator(n):
    """
    The collatz function creates a generator for the collatz conjecture
    starting at n and ending when n == 1.
    Each step yields the tuple (step, n) where
      step is the step number
      n is the current value
    """
    step = 0
    while n != 1:
        yield (step, n)
        # if n is even, divide n by 2
        if n % 2 == 0:
            n = n // 2
        # if n is odd, multiply n by 3 then add 1
        else:
            n = n * 3 + 1
        step += 1


def collatz(n):
    step = 0
    while n != 1:
        # if n is even, divide n by 2
        if n % 2 == 0:
            n = n // 2
        # if n is odd, multiply n by 3 then add 1
        else:
            n = n * 3 + 1
        step += 1
    return step


# one obvious pattern to observe: when we hit _any_ power of 2, the sequence becomes linear and will complete from that point in log2 of n steps. How to predict the point where the collatz conjecture will land on this path thought, that doesn't seem so obvious.
