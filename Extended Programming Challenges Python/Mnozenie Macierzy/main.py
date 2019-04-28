STARTUPINFO = """
print('First Matrix will be multiplied by Second Matrix, if some of the rows are smaller they will be completed by 0 at the ends of rows')
"""

class Matrix(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Entered values must be an ints!'
              '\nPrint end after typing :')

        matrix = self.func(*args, **kwargs)
        return matrix

@Matrix
def writerows(sizeerror = False, matrixshape = None):

    matrix = {}
    rownum = 0

    rows_max_length = 0
    cols_max_length = 0

    if sizeerror:
        rows_max_length = getRows(matrixshape)
        cols_max_length = getCols(matrixshape)

    while True:
        row = input().split(' ')

        if sizeerror:
            if len(row) > rows_max_length:
                print('row in the second matrix is too long put it again!')
                continue

        if row == ['end'] and sizeerror == False:
            return matrix
        else:
            try:
                row = map(int, row)
                row = list(row)
            except ValueError:
                print('Wrong values detected, try to input matrix again')
                del row
                continue

            matrix[rownum] = row
            rownum += 1

            if sizeerror:
                if rownum == cols_max_length:
                    return matrix

def getRows(matrix):
    return list(matrix.keys())[-1] + 1

def getCols(matrix):
    return len(matrix[0])


def autocomplete(matrix):
    row_biggest_length = max(len(val) for val in matrix.values())

    for row in matrix.values():
        if row_biggest_length > len(row):
            deficit = row_biggest_length - len(row)

            for i in range(deficit):
                row.append(0)

    return matrix


class Calculate(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.final = {}

    def multiply(self):
        res = 0
        listofvalues = []
        biggerkeymatrix = Calculate.getBiggerMatrix(self)

        for i in range(biggerkeymatrix):
            for v2 in self.second.values():
                itr2 = iter(v2)

                for v1 in self.first.values():
                    itr1 = iter(v1)

                    for j in range(i):
                        next(itr1)

                    res += next(itr1) * next(itr2)

                listofvalues.append(res)
                res = 0

        self.final = Calculate.concat(self, listofvalues, biggerkeymatrix)
        return self.final

    def concat(self, listofvalues, biggerkeymatrix):
        row = 0
        for col in range(biggerkeymatrix):
            self.final[row] = []
            for val in listofvalues[row::biggerkeymatrix]:
                self.final[row].append(val)
            row += 1

        return self.final

    def getBiggerMatrix(self):
        if list(self.first.keys())[-1] > list(self.second.keys())[-1]:
            return list(self.first.keys())[-1] + 1
        else:
            return list(self.second.keys())[-1] + 1


if __name__ == '__main__':
    exec(STARTUPINFO)
    first = autocomplete(writerows())
    second = autocomplete(writerows(sizeerror=True, matrixshape=first))
    result = Calculate(first, second)
    print(result.multiply())



