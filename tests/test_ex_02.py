import unittest
from exercises.ex_02 import find_numbers  # Adjust the import path as needed


class TestFindNumbers(unittest.TestCase):
    def test_basic_range(self):
        result = find_numbers(1, 50)
        expected = [7, 14, 21, 28, 42, 49]
        self.assertEqual(result, expected)

    def test_no_valid_numbers(self):
        result = find_numbers(1, 6)
        self.assertEqual(result, [])

    def test_single_valid_number(self):
        result = find_numbers(7, 7)
        self.assertEqual(result, [7])

    def test_large_range(self):
        result = find_numbers(2000, 3200)
        self.assertTrue(all(num % 7 == 0 and num % 5 != 0 for num in result))
        self.assertTrue(all(2000 <= num <= 3200 for num in result))

    def test_min_greater_than_max(self):
        result = find_numbers(50, 1)
        self.assertEqual(result, [])

    def test_negative_numbers(self):
        result = find_numbers(-50, -1)
        expected = [-49, -42, -35, -28, -21, -14, -7]
        self.assertEqual(result, expected)

    def test_zero_included(self):
        result = find_numbers(-10, 10)
        expected = [-7, 7]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
