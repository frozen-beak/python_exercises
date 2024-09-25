import unittest
import time
from exercises.ex_11 import sum_of_squares


class TestSumOfSquares(unittest.TestCase):

    def squares(self, n):
        return sum(i * i for i in range(n + 1))

    def test_basic_case(self):
        n = 10
        self.assertEqual(sum_of_squares(n), self.squares(n))

    def test_zero_case(self):
        n = 0
        self.assertEqual(sum_of_squares(n), self.squares(n))

    def test_single_digit_case(self):
        n = 4
        self.assertEqual(sum_of_squares(n), self.squares(n))

    def test_large_case(self):
        n = 1000
        self.assertEqual(sum_of_squares(n), self.squares(n))

    def test_performance(self):
        large_input = 10**6

        start_time = time.time()
        user_result = sum_of_squares(large_input)
        user_time = time.time() - start_time

        start_time = time.time()
        result_reference = self.squares(large_input)
        reference_time = time.time() - start_time

        self.assertEqual(user_result, result_reference)

        self.assertLess(
            user_time,
            reference_time,
            f"Your function is slower than the reference solution.\nYour time: {user_time:.6f}, Reference time: {reference_time:.6f}",
        )


if __name__ == "__main__":
    unittest.main()
