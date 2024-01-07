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
        # get ascending and descending arrangements using monotonic queues
        #   in linear time
        # BUG: 8082 becomes 2088 and 8802 instead of 0288 and 8820
        current = str(n)
        increasing = deque()
        decreasing = deque()
        for digit in current:
            print(digit, increasing, decreasing)
            if len(increasing) > 0 and int(digit) >= int(increasing[-1]):
                increasing.append(digit)
                decreasing.appendleft(digit)
            else:
                decreasing.append(digit)
                increasing.appendleft(digit)
        print(n, current, increasing, decreasing)
        # calculate next number in sequence
        n = int(''.join(decreasing)) - int(''.join(increasing))
        # count step
        total_steps = total_steps + 1 
        sleep(delay)
    return total_steps
