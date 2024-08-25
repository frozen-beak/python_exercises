import unittest
import sys
import os

from exercises.ex_01 import hello


class TestHelloFunction(unittest.TestCase):
    def test_hello_returns_correct_string(self):
        self.assertEqual(hello(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
