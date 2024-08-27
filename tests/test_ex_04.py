import unittest
from exercises.ex_04 import get_squares


class TestGetSquares(unittest.TestCase):
    def test_negative_input(self):
        with self.assertRaises(
            ValueError, msg="A negative number as input should raise a ValueError"
        ):
            get_squares(-1)

    def test_string_input(self):
        with self.assertRaises(
            ValueError, msg="A string as input should raise a ValueError"
        ):
            get_squares("2")

    def test_float_input(self):
        with self.assertRaises(
            ValueError, msg="A float number as input should raise a ValueError"
        ):
            get_squares(3.1)

    def test_zero_input(self):
        with self.assertRaises(
            ValueError, msg="If n is not a positive integer, then raise a ValueError"
        ):
            get_squares(0)

    def get_correct_squares_for_10(self):
        self.assertEqual(
            get_squares(10),
            {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100},
            "Your code produced wrong output",
        )

    def get_correct_squares_for_1(self):
        self.assertEqual(
            get_squares(10),
            {1: 1},
            "Your code produced wrong output",
        )


if __name__ == "__main__":
    unittest.main()
