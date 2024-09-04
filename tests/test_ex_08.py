import unittest
from exercises.ex_08 import transpose_matrix


class TestTransposeMatrixFunction(unittest.TestCase):

    def test_basic_transpose(self):
        self.assertEqual(
            transpose_matrix([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]]
        )

    def test_square_matrix(self):
        self.assertEqual(transpose_matrix([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_single_row(self):
        self.assertEqual(transpose_matrix([[1, 2, 3]]), [[1], [2], [3]])

    def test_single_column(self):
        self.assertEqual(transpose_matrix([[1], [2], [3]]), [[1, 2, 3]])

    def test_empty_matrix(self):
        self.assertEqual(transpose_matrix([]), [])

    def test_invalid_non_rectangular_matrix(self):
        with self.assertRaises(ValueError, msg="Matrix is not rectangular"):
            transpose_matrix([[1, 2, 3], [4, 5]])

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(ValueError, msg="Matrix contains non-numeric values"):
            transpose_matrix([[1, 2, "x"], [4, 5, 6]])

    def test_none_input(self):
        with self.assertRaises(ValueError, msg="Input is not a matrix"):
            transpose_matrix(None)


if __name__ == "__main__":
    unittest.main()
