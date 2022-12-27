# Jacobus Burger (2022)
# Info:
#   A collection of functions and classes to better understand and
#   just have fun with linear algebra.
# Sources:
#   https://www.andreinc.net/2021/01/20/writing-your-own-linear-algebra-matrix-library-in-c#row-echelon-form
#   https://stattrek.com/matrix-algebra/echelon-transform.aspx?tutorial=matrix
#   http://lampx.tugraz.at/~hadley/num/ch2/2.3a.php
#   https://www.youtube.com/watch?v=FAnNBw7d0vg
#   https://en.wikipedia.org/wiki/Norm_(mathematics)
#   https://en.wikipedia.org/wiki/Dot_product
import operator as op
from itertools import product


# NOTE I still want Identity matrix to be identified as a kind of matrix, so
#   figure out a way to maintain that equivalence across subclassing
# NOTE Vectors are a kind of matrix too aren't they? Maybe I should redefine
#   the matrix class into a generalized Tensor class and have arbitrary
#   dimensions fed into it as a dim attribute holding a list of dimensions?
# NOTE Figure out how to subscript the matrix class itself





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
        I = [
            1 if i == j else 0
            for j in range(rows)
            for i in range(columns)
        ]
        self.M = [
            elements[i]
            if i < len(elements)
            else I[i]
            for i in range(rows * columns)
        ]


    def __len__(self):
        return len(self.M)


    def __iter__(self):
        for element in self.M:
            yield element


    def __getitem__(self, index):
        y, x = index
        return self.M[y * self.n + x]


    def __setitem__(self, index, item):
        y, x = index
        self.M[y * self.n + x] = item


    # TODO improve formatting to handle many digits
    def __str__(self):
        string = ""
        for i in range(self.m):
            string += ' '.join(map(str, self.row(i))) + '\n'
        return '\n' + string 


    # A + B
    def __add__(self, other):
        C = self.copy()
        if type(other) != Matrix:
            # scalar + matrix
            for index, element in enumerate(C):
                C.M[index] = element + other
        else:
            # matrix + matrix
            for i, a, b in zip(range(len(self)), self, other):
                C.M[i] = a + b
        return C


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


    # A**n aka A * A n times (also includes inverse?)
    def __pow__(self, n):
        pass


    # -A
    def __neg__(self):
        return Matrix(self.m, self.n, *map(op.neg, self.M))


    # +A
    def __pos__(self):
        return Matrix(self.m, self.n, *map(op.pos, self.M))


    # | A |
    def __abs__(self):
        return Matrix(self.m, self.n, *map(op.abs, self.M))



    # A == B
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):
            if a != b:
                return False
        return True


    # create a new object with all the same attributes
    def copy(self):
        return Matrix(self.m, self.n, *self.M)


    # return first [i, j] position of first matching object
    def index(self, object):
        for index, element in enumerate(self):
            if element == object:
                # [i, j] aka [row, col]
                return [index // self.n, index % self.n]


    # return object at index
    def value(self, i, j):
        assert (i < self.m and j < self.n)
        return self.M[i * self.n + j]


    # return a list of elements in the row
    def row(self, i):
        assert (i < self.m)
        return self.M[i * self.n : i * self.n + self.n]

    
    # return a list of elements in the column
    def col(self, j):
        assert (j < self.n)
        return [self.M[i * self.n + j] for i in range(self.m)]


    # dot product
    def dot(self, other):
        pass


    # matrix transposition
    def transpose(self):
        pass


    # matrix determinant
    def det(self):
        pass


    # reduced eschelon form
    def ref(self):
        pass


    # row reduced eschelon form
    def rref(self):
        pass


    # LU(P) decomposition
    def LU(self):
        pass


    # QR decomposition
    def QR(self):
        pass


    # forward subsitution to solve linear systems of form Lx = B
    def forward(self):
        pass


    # backward substitution to solve linear systems of form Ux = Y
    def backward(self):
        pass


    # LU(P) decomposition to solve linear systems of form Ax = B
    def LU_solve(self):
        pass
