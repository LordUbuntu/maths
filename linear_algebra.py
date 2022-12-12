# Jacobus Burger (2022)
# A collection of functions and classes for practicing linear algebra





# matrix class (may generalize to tensor once I know what that is lol)
class Matrix:
    def __doc__(self):
        return """
    Matrix Class
        This class represents m by n matrices.
        m = the number of rows in the matrix
        n = the number of columns in the matrix
        M = the matrix itself

        What is particularly special about this class and its derivatives
        is how the matrix is represented. Rather than using a dictionary
        with (i,j) coordinates or a multidimensional array, we can
        represent the matrix as a one-dimensional array that is
        n*m elements long. Accessing elements is also very interesing,
        we use a simple calculation to get the ith row and jth column.

    How the math works:
        First imagine a 2D 2 by 2 array:

        A = [[1, 2], [3, 4]]

        We'll notice here that to get row 1 we do A[0], and to get
        column 1 we do A[i][0]. Notice however that to get any element
        in the row we're essentially dictating an offset on the ith
        and jth axes of the matrix. Now imagine a 1D 2 by 2 array:

        A = [1, 2, 3, 4]

        Notice that if we iterate through these elements from left to
        right they map exactly to each element of a matrix if we read
        it left-to-right and top-to-bottom:

        1 2
        3 4

        If we wanted to get element 3 from index 0 (element 1), all
        we would need to do is offset the index of element 1 by the
        column dimension n. So to get the first element in row i would
        be A[i * n]. Following from this, if we wanted to get the jth
        element within that row, we would only need to add an offset
        of j like A[i * n + j].

        Eg: element 2 == A[0 * 2 + 1]

        This allows us to calculate any row then as a slice starting
        at the beginning of a given row i times the offset (number of
        columns n) and ending at that point plus the number of columns 
        for a given row n. For instance, the first element of row 0
        would be A[0 * 2 + 0], and the last element would be 
        A[0 * 2 + n]. This can be simplified as start = A[0 * 2] 
        and end = A[0 * 2 + n]. So putting all of this together 
        we get the ith row with:

        row = [i * 2 : i * 2 + n]

        But the mathematical benefits of this representation don't stop
        at getting whole rows in a single O(1) step, we can also get
        an entire row in a single O(n) step too! To do this, first we
        need to realize again that to get the jth element in the ith
        row we do A[i * n + j]. So if we want the jth row, then we only
        need to do this forall i in m (for all rows in the column j).
        To do that:

        for i in range(m):
            col += A[i * n + j]

        Or as a list comprehension:

        col = [A[i * n + j] for i in range(m)]

        The benefit of this is that we don't require nested loops
        to find the rows or columns of the matrix, and in many
        cases we can take a slice or directly access an element, both
        of which are O(1) operations. Additionally, this allows for a
        high degree of flexiblity that might enable tensors of higher
        dimensions as well (though I haven't figured that out yet), and
        determining the index of an element at the ith row and jth
        column are also O(1) complexity, since they're a simple math
        calculation. Lastly, because Python arrays can contain anything,
        that means that the matrices constructed will themselves be
        flexible to contain any type (which might be incredibly powerful).
    """


    def __init__(self, rows, columns, *elements):
        self.m = rows
        self.n = columns
        self.M = [
            elements[i]
            if i < len(elements) else 0
            for i in range(rows * columns)
        ]


    # TODO improve formatting to handle many digits
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
    def __doc__(self):
        return """
    Identity Matrix:
        This is a specialized variation of the Matrix class which
        produces a square n by n Identity matrix.
        n = the square dimension of the matrix
    """


    def __init__(self, n):
        self.m = n
        self.n = n
        self.M = [1 if i == j else 0 for j in range(n) for i in range(n)]
