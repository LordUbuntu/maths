# Jacobus Burger (2024)
# kaprekar's constant, one of many numbers whose ordered sums in sequence
#   eventually return to the same number as was started.
# there are many numbers like kaprekar's constant for sets of numbers
#   with different digits and division operations. I'm asounded by the
#   mystery of these numeric cycles, though I don't know how much I
#   don't know.
# see:
#   https://en.wikipedia.org/wiki/6174
#   https://brilliant.org/wiki/kaprekars-constant/
from collections.abc import Generator
from time import sleep

KAPREKAR_CONSTANT = 6174


def count_steps(n: int, delay: int = 0) -> int:
    """Count the steps between 'n' and the Kaprekar constant."""
    total_steps = 0
    while n != KAPREKAR_CONSTANT:
        # sort into increasing and decreasing numeric arrangement
        digits = [*str(n)]
        increasing = sorted(digits)
        decreasing = sorted(digits, reverse=True)
        # calculate next number in sequence
        n = int("".join(decreasing)) - int("".join(increasing))
        # count step
        total_steps = total_steps + 1
        sleep(delay)
    return total_steps


def generate_sequence(n: int) -> Generator[int]:
    """Yield numbers between n to the Kaprekar constant."""
    yield n
    while n != KAPREKAR_CONSTANT:
        # sort into increasing and decreasing numeric arrangement
        digits = [*str(n)]
        increasing = sorted(digits)
        decreasing = sorted(digits, reverse=True)
        # generate next number in sequence
        n = int("".join(decreasing)) - int("".join(increasing))
        yield n


def show_iterations(n: int) -> None:
    """Print the sequence from n to the Kaprekar constant."""
    print(n)
    while n != KAPREKAR_CONSTANT:
        # sort into increasing and decreasing numeric arrangement
        digits = [*str(n)]
        increasing = sorted(digits)
        decreasing = sorted(digits, reverse=True)
        # generate next number in sequence
        n = int("".join(decreasing)) - int("".join(increasing))
        print(f"{''.join(decreasing)} - {''.join(increasing)} = {n}")
