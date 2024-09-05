import unittest
from exercises.ex_09 import multiply_matrices


class TestMatrixMultiplicationFunction(unittest.TestCase):

    def test_basic_multiplication(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        result = [[19, 22], [43, 50]]
        self.assertEqual(multiply_matrices(matrix1, matrix2), result)

    def test_multiplication_with_different_sizes(self):
        matrix1 = [[1, 4, 7], [2, 5, 8]]
        matrix2 = [[1, 2], [3, 4], [5, 6]]
        result = [[48, 60], [57, 72]]
        self.assertEqual(multiply_matrices(matrix1, matrix2), result)

    def test_single_element_matrices(self):
        self.assertEqual(multiply_matrices([[3]], [[4]]), [[12]])

    def test_empty_matrix(self):
        self.assertEqual(multiply_matrices([], []), [])

    def test_invalid_size_for_multiplication(self):
        with self.assertRaises(ValueError, msg="Matrix multiplication is not possible"):
            multiply_matrices([[1, 2]], [[1, 2], [3, 4], [5, 6]])

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(ValueError, msg="Matrices contain non-numeric values"):
            multiply_matrices([[1, 2], [3, "x"]], [[4, 5], [6, 7]])

    def test_none_input(self):
        with self.assertRaises(ValueError, msg="Input matrices are not valid"):
            multiply_matrices(None, None)


if __name__ == "__main__":
    unittest.main()
