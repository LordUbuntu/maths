# Jacobus Burger (2022)
# Info:
#   Bordering on a library which I've written to better understand how to implement Linear Algebra, also a fun way to learn new LA info
#   and brush up on old info as well.
# Sources:
#   https://www.andreinc.net/2021/01/20/writing-your-own-linear-algebra-matrix-library-in-c#row-echelon-form
#   https://stattrek.com/matrix-algebra/echelon-transform.aspx?tutorial=matrix
#   http://lampx.tugraz.at/~hadley/num/ch2/2.3a.php
#   https://www.youtube.com/watch?v=FAnNBw7d0vg
#   https://en.wikipedia.org/wiki/Norm_(mathematics)
#   https://en.wikipedia.org/wiki/Dot_product
import operator as op
from itertools import product, repeat
from functools import reduce





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


    def __repr__(self):
        # get formatting width of the cells
        width = max(map(len, map(str, self.M)))
        # represent matrix as string
        string = ""
        for i in range(0, len(self.M), self.n):
            # make each row an equally spaced string
            string += ' '.join([
                            n.ljust(width)
                            for n in map(str, self.M)
                        ][i:i + self.n]) + '\n'
        return string


    # A op B
    # I realized that many of the binary operations use repeated code
    def bin_op(self, other, op):
        C = self.copy()
        if type(other) != Matrix:
            # scalar op matrix
            C.M = list(map(op, self, repeat(other)))
        else:
            # matrix op matrix
            C.M = list(map(op, self, other))
        return C

    # A + B
    def __add__(self, other):
        return self.bin_op(other, op.add)


    # A - B
    def __sub__(self, other):
        return self.bin_op(other, op.sub)


    # A // B
    def __floordiv__(self, other):
        return self.bin_op(other, op.floordiv)


    # A / B
    def __truediv__(self, other):
        return self.bin_op(other, op.truediv)


    # A * B
    def __mul__(self, other):
        pass  # needs specialized implementation


    # A**n aka A * A n times (also includes inverse?)
    def __pow__(self, n):
        return reduce(Matrix.dot, [self for _ in range(n)])


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
        return all(map(op.eq, self, other))


    def __ne__(self, other):
        return not self.__eq__(other)


    def __lt__(self, other):
        if len(self) != len(other):
            return False
        return all(map(op.lt, self, other))


    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


    def __gt__(self, other):
        return not self.__lt__(other)


    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


    # create a new object with all the same attributes
    def copy(self):
        return Matrix(self.m, self.n, *self.M)


    # return first [i, j] position of first matching object
    def index(self, object):
        for index, element in enumerate(self):
            if element == object:
                # [i, j] aka [row, col]
                return [index // self.n, index % self.n]
        return -1


    # return object at index
    def value(self, i, j):
        return self[i, j]


    # return a list of elements in the row
    def row(self, i):
        return self.M[i * self.n : i * self.n + self.n]

    
    # return a list of elements in the column
    def col(self, j):
        return [self.M[i * self.n + j] for i in range(self.m)]


    # dot product (matrix multiplication) - neiive solution
    def dot(self, other):
        if self.n == other.m:
            C = Matrix(self.m, other.n, *self)
            for i in range(self.m):
                for j in range(other.n):
                    C.M[i] = reduce(op.add, map(op.mul, self.row(i), self.col(j)))
            return C



    # matrix transposition
    def transpose(self):
        N = [element for j in range(self.m) for element in self.col(j)]
        A = Matrix(self.n, self.m, *N)
        return A


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
