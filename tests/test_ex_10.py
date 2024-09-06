import unittest
from exercises.ex_10 import is_binary_divisible_by_5


class TestBinaryDivisibilityBy5(unittest.TestCase):

    def test_basic_divisibility_true(self):
        self.assertTrue(is_binary_divisible_by_5("10100"))  # 20 in base10

    def test_basic_divisibility_false(self):
        self.assertFalse(is_binary_divisible_by_5("1001"))  # 9 in base10

    def test_single_bit(self):
        self.assertFalse(is_binary_divisible_by_5("1"))  # 1 in base10
        self.assertTrue(is_binary_divisible_by_5("0"))  # 0 in base10

    def test_invalid_binary_characters(self):
        with self.assertRaises(ValueError, msg="Invalid binary string"):
            is_binary_divisible_by_5("10102")

    def test_empty_input(self):
        with self.assertRaises(ValueError, msg="Empty input"):
            is_binary_divisible_by_5("")

    def test_none_input(self):
        with self.assertRaises(ValueError, msg="Input is not a valid string"):
            is_binary_divisible_by_5(None)


if __name__ == "__main__":
    unittest.main()
