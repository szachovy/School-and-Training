import unittest
import main
import re

class MatrixRowsVerification(unittest.TestCase):
    def setUp(self):
        self.matrix1 = {0: [1, 2, 3], 1: [4, 5, 6]}
        self.matrix2 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}

    def test_getRowsType(self):
        self.assertIsInstance(main.getRows(self.matrix1), int, 'wrong type of returned number of rows')

    def test_getRowsNonNegative(self):
        self.assertGreaterEqual(main.getRows(self.matrix1), 0, 'rows of matrix cannot be negative number')

    def test_getRowsVerification(self):
        self.assertEqual(main.getRows(self.matrix1), 2, 'returned number of rows isnt correct')
        self.assertEqual(main.getRows(self.matrix2), 3, 'returned number of rows isnt correct')

class MatrixColsVerification(unittest.TestCase):
    def setUp(self):
        self.matrix1 = {0: [1, 2, 3], 1: [4, 5, 6]}
        self.matrix2 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}

    def test_getColsType(self):
        self.assertIsInstance(main.getCols(self.matrix1), int, 'wrong type of returned number of columns')

    def test_getColsNonNegative(self):
        self.assertGreaterEqual(main.getCols(self.matrix1), 0, 'rows of matrix cannot be negative number')

    def test_getColsVerification(self):
        self.assertEqual(main.getCols(self.matrix1), 3, 'returned number of rows isnt correct')
        self.assertEqual(main.getCols(self.matrix2), 2, 'returned number of rows isnt correct')

class AutocompleteVerification(unittest.TestCase):
    def test_autocomplete(self):
        matrix = {0: [1, 2, 3], 1: [4], 2: [5, 6]}
        expectedmatrix = {0: [1, 2, 3], 1: [4, 0, 0], 2: [5, 6, 0]}
        self.assertEqual(main.autocomplete(matrix), expectedmatrix, 'autocomplete zeros not handled')


class WrongInputException(Exception):
    pass

class WriteRowsVerification(unittest.TestCase):
    def setUp(self):
        self.matrix = main.writerows()

    def test_wrong_input(self):
        self.assertTrue(re.findall(r"[A-Za-z]*$", str(self.matrix.values())), 'Letters in matrix has been found')

    def test_returnsDict(self):
        try:
            self.assertIsInstance(self.matrix, dict)
        except WrongInputException:
            self.fail('writing rows doesnt format matrix (dict with rows and cols)')


class VerifyFinalMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix1 = {0: [1, 2, 3], 1: [4, 5, 6]}
        self.matrix2 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
        self.final = {0: [9, 12, 15], 1: [19, 26, 33], 2: [29, 40, 51]}

    def test_checkFinal(self):
        self.assertEqual(main.Calculate(self.matrix1, self.matrix2).multiply(), self.final, 'Unexpected final matrix '
                                                                                            'after calculations')

    def tearDown(self):
        self.final.clear()

if __name__ == '__main__':
    unittest.main()
