# Jacobus Burger (2022)
# Interactive calculators and various functions for financial accounting.
# Made for the fun of learning and conveneince.
from collections import deque

# TODO: More to add
# Assets = Liabilities + Owner Equity + Revenue - Expenses - Owner Draws
# Income, Expenses, Fixed and Variable Cost, Total Equity, Inventory, Cost of Goods Sold, Sales Expenses, and More.
# TODO:
# Split it up!


def operating_cycle(days_sales_in_inventory, collection_priod):
    return days_sales_in_inventory + collection_period


# interactive calculator for FIFO COGS
def fifo_cogs():
    """calculate cost of good sold using FIFO method interactively"""
    inventory = deque([])
    total = 0
    while True:
        prompt = input()
        if prompt == "+":
            # add item to inventory
            units, cost_per_unit = [int(n) for n in input().split(",")]
            inventory_queue.append([units, cost_per_unit])
        if prompt == "-":
            # calculate COGS for units
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


# interactive calculator for WA COGS
def wa_cogs():
    """calculate cost of goods sold using Weighted Average method interactively"""
    inventory = []
    total_cogs = 0
    while True:
        prompt = input()
        if prompt == "+":
            # add item to inventory
            units, cost_per_unit = [int(n) for n in input().split(",")]
            inventory.append([units, cost_per_unit])
        if prompt == "-":
            # calculate weighted average of total list so far
            total_units = sum([item[0] for item in inventory])
            total_cost_per_units = 0
            for i in range(len(inventory)):
                total_cost_per_units += inventory[i][0] * inventory[i][1]
            average_cost_per_unit = total_cost_per_units / total_units
            inventory = [[total_units, average_cost_per_unit]]
            # calculate cogs
            units = int(input())
            inventory[0][0] -= units
            total_cogs += units * inventory[0][1]
        if prompt == "q":
            return total_cogs
        print(total_cogs)


# start program on the assumption that user wants interactive COGS calculation (useful for my case)
if __name__ == "__main__":
    method = int(
        input(
            """
        what method would you like to calculate COGS?
        1) FIFO
        2) WA
    """
        )
    )
    if method == 1:
        print(fifo_cogs())
    if method == 2:
        print(wa_cogs())
