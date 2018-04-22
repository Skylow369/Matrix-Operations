import copy
import random


class Matrix:
    def __init__(self, matrix=None, numrows=0, numcols=0):
        self.numrows = numrows
        self.numcols = numcols
        self.rows = []
        self.columns = []
        self.setvals(matrix)

    def printmatrix(self):
        print("Matrix:")
        for i in self.rows:
            print(i)
        print("")

    def setvals(self, mat=None):
        if mat is None:
            if self.numrows == 0 and self.numcols == 0:
                self.numrows = int(input("Number of rows: "))
                self.numcols = int(input("Number of columns: "))
            print("\nSeparate numbers by one space and round decimals to the nearest thousandth")
            for i in range(self.numrows):
                vals = input("Row " + str(i+1) + ": ")
                row = list(map(float, vals.split(' ')))

                if len(row) != self.numcols:
                    print("Incorrect number of values")
                    return
                self.rows.append(row)

        else:
            self.rows = mat
            self.numrows = len(mat)
            self.numcols = len(mat[0])

        for i in range(self.numcols):
            self.columns.append([])

        for i in range(len(self.rows)):
            for x in range(len(self.rows[0])):
                self.columns[x].append(self.rows[i][x])
        print("")

    def inverse(self):
        mat = copy.deepcopy(self.columns)
        if len(mat) != len(mat[0]):
            print("Matrix needs to be a square matrix\n")
            return

        d = self.determinant(mat)

        if len(mat) == 2 and len(mat[0]) == 2:
            mat = copy.deepcopy(self.rows)
            mat[0][0], mat[1][1] = mat[1][1], mat[0][0]
            mat[0][1] *= -1
            mat[1][0] *= -1

            for i in range(len(mat)):
                for x in range(len(mat[0])):
                    mat[i][x] *= (1/d)
                    mat[i][x] = round(mat[i][x], 3)
            mat = Matrix(mat)
            return mat

        inmat = copy.deepcopy(mat)
        for i in range(len(mat)):
            for x in range(len(mat[0])):
                minor = self.minor(i, x, mat)
                inmat[i][x] = ((-1)**(i + x)) * self.determinant(minor)
                inmat[i][x] *= (1/d)
                inmat[i][x] = round(inmat[i][x], 3)

        inmat = Matrix(inmat)
        return inmat

    def minor(self, row, column, matrix):
        minor = copy.deepcopy(matrix)
        minor.pop(row)

        for i in range(len(minor)):
            minor[i].pop(column)

        return minor

    def determinant(self, mat=None):
        if mat is None:
            mat = self.rows

        if len(mat) == 2 and len(mat[0]) == 2:
            return (mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0])

        if len(mat) != len(mat[0]):
            print("Matrix needs to be a square matrix\n")
            return

        determinant = 0

        for i in range(len(mat[0])):
            minor = copy.deepcopy(mat)
            minor = self.minor(0, i, minor)

            if i % 2 == 0:
                determinant += mat[0][i] * self.determinant(minor)
            else:
                determinant -= mat[0][i] * self.determinant(minor)

        return determinant

    def __add__(self, other):
        if self.numrows != other.numrows or self.numcols != other.numcols:
            print("Cannot add matrices\n")
            return

        newmat = []
        for i in range(self.numrows):
            newmat.append([])
            for x in range(self.numcols):
                newmat[i].append(self.rows[i][x] + other.rows[i][x])

        newmat = Matrix(newmat)
        return newmat

    def __sub__(self, other):
        if self.numrows != other.numrows or self.numcols != other.numcols:
            print("Cannot subtract matrices\n")
            return

        newmat = []
        for i in range(self.numrows):
            newmat.append([])
            for x in range(self.numcols):
                newmat[i].append(self.rows[i][x] - other.rows[i][x])

        newmat = Matrix(newmat)
        return newmat

    def __mul__(self, other):
        if type(other) == int:
            for i in range(self.numrows):
                for x in range(self.numcols):
                    self.rows[i][x] *= other

            for i in range(len(self.columns)):
                for x in range(len(self.columns[0])):
                    self.columns[i][x] *= other
            self.printmatrix()
            return

        if type(other) == Matrix:
            if len(self.columns) != len(other.rows):
                print("Cannot multiply matrices\n")
                return

            newmat = []
            for i in range(self.numrows):
                newmat.append([])
            count = 0
            sum = 0
            for row in range(self.numrows):
                for col in range(other.numcols):
                    while count < self.numcols:
                        sum += self.rows[row][count] * other.columns[col][count]
                        count += 1
                    newmat[row].append(round(sum, 3))
                    sum = 0
                    count = 0

            newmat = Matrix(newmat)
            return newmat

