# Task: Create a "custom Datatype" Matrix that
#   a) is initiated with a constant value and the number of rows and cols
#   b) when printed to the terminal it should be displayed as a matrix
#   c) values should be received or set with typing a[i,j]
#   d) handle mulitplication of two matrices with the *-operator


class Matrix:
    def __init__(self, value, rows, cols):

        mat = []

        for row in range(rows):
            rowVals = []
            for col in range(cols):
                rowVals += [value]
            mat += [rowVals]

        self.values = mat
        self.rows = rows
        self.cols = cols
        # self.val = value

    # Matrix[index]
    def __getitem__(self, index):
        return self.values[index[0]][index[1]]

    # Matrix[index] = val
    def __setitem__(self, index, val):
        self.values[index[0]][index[1]] = val

    def __repr__(self):
        mat = ""
        for i in range(self.rows):
            for j in range(self.cols):
                mat += str(self.values[i][j]) + "  "
            mat += "\n"

        return mat
        # return "%sx%s-Matrix, Values: %s" % (self.rows, self.cols, self.values)

    def __mul__(self, other):
        if (self.cols != other.rows):
            raise Exception(
                "to mulitply two matrixes A.cols has to equal B.rows")

        # colcount of self has to equal rowcount of other = n
        # cij = sum(k=1 to k=n) aik*bkj
        res = Matrix(0, self.rows, other.cols)

        for i in range(res.rows):
            for j in range(res.cols):
                acc = 0
                for k in range(self.cols):
                    acc += self[i, k]*other[k, j]

                res[i, j] = acc

        return res


# test
m = Matrix(0, 6, 4)
m[0, 2] = 1
m[1, 2] = 3
m[3, 3] = 1
print(m)
n = Matrix(2, 4, 2)
print(n)
print(m*n)
