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


    # A + B
    def __add__(self, other):
        pass


    # A - B
    def __sub__(self, other):
        pass


    # A * B
    def __mul__(self, other):
        pass


    # A // B
    def __floordiv__(self, other):
        pass


    # A / B
    def __truediv__(self, other):
        pass


    # A**n aka A * A n times
    def __pow__(self, n):
        pass


    # -A
    def __neg__(self):
        pass


    # +A
    def __pos__(self):
        pass


    # | A |
    def __abs__(self):
        pass


    # A == B
    def __eq__(self, other):
        pass


    # TODO figure out how to handle access out of bounds
    def row(self, n):
        return self.M[n * self.n : n * self.n + self.n]

    
    # TODO figure out how to handle access out of bounds
    def col(self, n):
        return [self.M[self.n * i + n] for i in range(self.m)]


    def dot(self, other):
        pass


    def transpose(self):
        pass





class Identity(Matrix):
    def __init__(self, n):
        self.m = n
        self.n = n
        self.M = [1 if i == j else 0 for j in range(n) for i in range(n)]
