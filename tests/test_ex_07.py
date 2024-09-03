import unittest
from exercises.ex_07 import sort_sequence


class TestSortWordsFunction(unittest.TestCase):

    def test_sort_basic(self):
        self.assertEqual(
            sort_sequence("without,hello,bag,world"), "bag,hello,without,world"
        )

    def test_sort_with_duplicates(self):
        self.assertEqual(
            sort_sequence("apple,banana,apple,orange"), "apple,banana,orange"
        )

    def test_sort_case_insensitive(self):
        self.assertEqual(sort_sequence("Banana,apple,Orange"), "apple,Banana,Orange")

    def test_sort_with_spaces(self):
        self.assertEqual(sort_sequence("  cat, dog ,bat "), "bat,cat,dog")

    def test_invalid_input_numbers(self):
        with self.assertRaises(ValueError, msg="Input contains invalid strings"):
            sort_sequence("apple,123,banana")

    def test_invalid_input_mixed_characters(self):
        with self.assertRaises(
            ValueError,
            msg="Input contains non alphabetical characters or special symbols",
        ):
            sort_sequence("apple,@banana,orange")

    def test_invalid_format_no_commas(self):
        with self.assertRaises(ValueError, msg="Input is not correctly formatted"):
            sort_sequence("apple banana orange")

    def test_empty_string(self):
        with self.assertRaises(ValueError, msg="Empty input is provided"):
            sort_sequence("")

    def test_none_input(self):
        with self.assertRaises(ValueError, msg="Provided input is not of type string"):
            sort_sequence(None)


if __name__ == "__main__":
    unittest.main()
