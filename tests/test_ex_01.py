import unittest
import sys
import os

# Add the parent directory to the Python path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.ex_01 import hello


class TestHelloFunction(unittest.TestCase):
    def test_hello_returns_correct_string(self):
        self.assertEqual(hello(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
