# Made by Jacobus Burger (2022)
# Various finance maths (personal finance, financial planning)
# For fun and education

def compound_interest(P, r, n, t):
    """calculate amount after compounding interest period"""
    return P * (1 + r/n)**(n*t)


# returns from mutual funds
def total_return(units,
        cost_per_unit,
        dividend_per_unit,
        interest_per_unit,
        closing_navps):
    opening   = units * cost_per_unit
    dividends = units * dividend_per_unit
    interest  = units * interest_per_unit
    closing   = units * closing_navps
    return ((closing - opening) + dividends + interest) / opening


def unrealized_capital_loss_or_gain(units, beginning_navps, ending_navps):
    return (units * beginning_navps) - (units * ending_navps)



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
        print(total_cogs)


def wa_cogs():
    # another interactive demo
    """calculate cost of goods sold using Weighted Average method interactively"""
    inventory = []
    total_cogs = 0
    while True:
        prompt = input()
        if prompt == "+":
            units, cost_per_unit = [int(n) for n in input().split(',')]
            inventory.append([units, cost_per_unit])
        if prompt == "-":
            # calculate weighted average of total list so far
            total_units = sum([item[0] for item in inventory])
            total_cost_per_units = 0
            for i in range(len(inventory)):
                total_cost_per_units += (inventory[i][0] * inventory[i][1])
            average_cost_per_unit = total_cost_per_units / total_units
            inventory = [[total_units, average_cost_per_unit]]

            # calculate cogs
            units = int(input())
            inventory[0][0] -= units
            total_cogs += (units * inventory[0][1])
        if prompt == "q":
            return total_cogs
        print(total_cogs)
