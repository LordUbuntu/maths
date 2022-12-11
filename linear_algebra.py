# Jacobus Burger (2022)
# A collection of functions and classes for practicing linear algebra





# matrix class (may generalize to tensor once I know what that is lol)
class Matrix:
    def __init__(self, rows, columns, *elements):
        self.m = rows
        self.n = columns
        self.M = [*elements]


    def __str__(self):
        string = ""
        for i in range(self.m):
            string += '\n' + ' '.join(map(str, self.row(i)))
        return string


    def row(self, n):
        # TODO figure out how to handle access out of bounds
        return self.M[n * self.m : n * self.m + self.n]
