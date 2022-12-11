# Jacobus Burger (2022)
# A collection of functions and classes for practicing linear algebra





# matrix class (may generalize to tensor once I know what that is lol)
class Matrix:
    def __init__(self, rows, columns, *elements):
        self.m = rows
        self.n = columns
        self.M = [
            elements[i]
            if i < len(elements) else 0
            for i in range(rows * columns)
        ]


    def __str__(self):
        string = ""
        for i in range(self.m):
            string += '\n' + ' '.join(map(str, self.row(i)))
        return string


    # TODO figure out how to handle access out of bounds
    def row(self, n):
        return self.M[n * self.n : n * self.n + self.n]

    
    # TODO figure out how to handle access out of bounds
    def col(self, n):
        return [self.M[self.n * i + n] for i in range(self.m)]
