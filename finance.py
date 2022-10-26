# Made by Jacobus Burger (2022)
# Various finance maths (personal finance, financial planning)
# For fun and education

def compound_interest(P, r, n, t):
    """calculate amount after compounding interest period"""
    return P * (1 + r/n)**(n*t)


def fifo_cogs():
    # more of a demo than a usable program
    """calculate cost of good sold using FIFO method interactively"""
    inventory_queue = []
    total_cogs = 0
    while True:
        prompt = input()
        if prompt == "+":
            units, cost_per_unit = [int(n) for n in input().split(',')]
            inventory_queue.append([units, cost_per_unit])
        if prompt == "-":
            units = int(input())
            for _ in range(units):
                if inventory_queue[0][0] - 1 <= 0:
                    total_cogs += inventory_queue.pop(0)[1]
                else:
                    total_cogs += inventory_queue[0][1]
                    inventory_queue[0][0] -= 1
        if prompt == "q":
            return total_cogs
