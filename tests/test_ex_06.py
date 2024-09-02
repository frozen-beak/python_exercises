import unittest
from exercises.ex_06 import gen_2d_array


class TestGen2DArray(unittest.TestCase):

    def test_typical_case(self):
        """Test a typical case with small positive integers."""
        self.assertEqual(
            gen_2d_array(3, 5), [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
        )

    def test_zero_rows(self):
        """Test with 0 rows, expecting an empty list."""
        self.assertEqual(gen_2d_array(0, 5), [])

    def test_zero_columns(self):
        """Test with 0 columns, expecting a list of empty lists."""
        self.assertEqual(gen_2d_array(3, 0), [[], [], []])

    def test_zero_rows_and_columns(self):
        """Test with 0 rows and 0 columns, expecting an empty list."""
        self.assertEqual(gen_2d_array(0, 0), [])

    def test_negative_values(self):
        """Test with negative dimensions, expecting a ValueError."""
        with self.assertRaises(ValueError):
            gen_2d_array(-1, 5)
        with self.assertRaises(ValueError):
            gen_2d_array(3, -5)

    def test_non_integer_inputs(self):
        """Test with non-integer inputs, expecting a ValueError."""
        with self.assertRaises(ValueError):
            gen_2d_array(3.5, 5)
        with self.assertRaises(ValueError):
            gen_2d_array(3, "5")

    def test_large_values(self):
        """Test with large values to check function efficiency and correctness."""
        result = gen_2d_array(1000, 1000)
        self.assertEqual(
            result[999][999], 999 * 999
        )  # Ensure calculation is correct for the largest value

    def test_mixed_edge_cases(self):
        """Test tricky combinations like 1 row, 0 columns and vice versa."""
        self.assertEqual(gen_2d_array(1, 0), [[]])
        self.assertEqual(gen_2d_array(0, 1), [])

    def test_single_row_and_column(self):
        """Test when there's only 1 row and 1 column."""
        self.assertEqual(gen_2d_array(1, 1), [[0]])


if __name__ == "__main__":
    unittest.main()
