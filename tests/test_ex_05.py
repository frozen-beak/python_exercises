import unittest
from exercises.ex_05 import calculate_eoq


class TestCalculateEOQ(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(calculate_eoq(180), 24, "Expected EOQ for D=180 is 24")

    def test_negative_input(self):
        with self.assertRaises(
            ValueError, msg="Negative input should raise a ValueError"
        ):
            calculate_eoq(-50)

    def test_zero_input(self):
        self.assertEqual(calculate_eoq(0), 0, "EOQ for D=0 should be 0")

    def test_large_input(self):
        self.assertEqual(
            calculate_eoq(1000000),
            1826,
            "EOQ for large D=1000000 should be rounded correctly",
        )

    def test_string_input(self):
        with self.assertRaises(
            ValueError, msg="A string as input should raise a ValueError"
        ):
            calculate_eoq("2")

    def test_special_character_input(self):
        with self.assertRaises(
            ValueError, msg="Special characters as input should raise a ValueError"
        ):
            calculate_eoq("$")

    def test_none_input(self):
        with self.assertRaises(
            ValueError, msg="None as input should raise a ValueError"
        ):
            calculate_eoq(None)

    def test_boolean_input(self):
        with self.assertRaises(
            ValueError, msg="A boolean as input should raise a ValueError"
        ):
            calculate_eoq(True)

    def test_unexpected_data_type_input(self):
        with self.assertRaises(
            ValueError, msg="A list as input should raise a ValueError"
        ):
            calculate_eoq([100])


if __name__ == "__main__":
    unittest.main()
