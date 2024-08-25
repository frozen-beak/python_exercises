import unittest
from exercises.ex_03 import calculate_factorial


class TestCalculateFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(calculate_factorial(0), 1, "Factorial of 0 should be 1")

    def test_factorial_one(self):
        self.assertEqual(calculate_factorial(1), 1, "Factorial of 1 should be 1")

    def test_factorial_positive_small(self):
        self.assertEqual(calculate_factorial(5), 120, "Factorial of 5 should be 120")

    def test_factorial_positive_medium(self):
        self.assertEqual(
            calculate_factorial(10), 3628800, "Factorial of 10 should be 3628800"
        )

    def test_factorial_positive_large(self):
        self.assertEqual(
            calculate_factorial(20),
            2432902008176640000,
            "Factorial of 20 should be 2432902008176640000",
        )

    def test_factorial_negative(self):
        with self.assertRaises(
            ValueError, msg="Factorial of negative numbers should raise ValueError"
        ):
            calculate_factorial(-5)

    def test_factorial_float(self):
        with self.assertRaises(
            ValueError, msg="Factorial of float numbers should raise ValueError"
        ):
            calculate_factorial(5.5)

    def test_factorial_string(self):
        with self.assertRaises(
            ValueError, msg="Factorial of strings should raise ValueError"
        ):
            calculate_factorial("5")

    def test_factorial_bool(self):
        with self.assertRaises(
            ValueError, msg="Factorial of boolean values should raise ValueError"
        ):
            calculate_factorial(True)

    def test_factorial_none(self):
        with self.assertRaises(
            ValueError, msg="Factorial of None should raise ValueError"
        ):
            calculate_factorial(None)

    def test_factorial_large_input(self):
        # This test checks if the function can handle large inputs without excessive runtime
        # You may need to adjust the input value based on your implementation's efficiency
        result = calculate_factorial(500)
        self.assertIsInstance(
            result, int, "Result should be an integer for large inputs"
        )
        self.assertGreater(result, 0, "Result should be positive for large inputs")


if __name__ == "__main__":
    unittest.main()
