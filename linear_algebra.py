# Jacobus Burger (2022)
# A collection of functions and classes for practicing linear algebra





# matrix class (may generalize to tensor once I know what that is lol)
class Matrix:
    def __init__(self, rows, columns, *elements):
        self.m = rows
        self.n = columns
        self.M = [*elements]
