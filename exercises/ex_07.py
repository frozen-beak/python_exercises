"""
# Sort Words

## Metadata
- Level: 2
- Title: Sort Words
- Topics: Sorting, String Operations

## Instructions
Implement a function called `sort_sequence(sequence)` that accepts a comma-separated string of words, 
validates the input, and returns the words in a comma-separated sequence after sorting them alphabetically.

## Example

Input: "without, hello, bag, world"
Output: "bag,hello,without,world"

## How to Test

Run the following command in your terminal:
```bash
python -m unittest tests.test_ex_07
```

## Hints:
- `sequence` is a string of words separated by commas(,).
- Any leading or trailing spaces in the words should be ignored.
- If the input contains non-alphabetical characters or is improperly formatted (e.g., missing commas), 
  the function should raise a `ValueError`.
- Duplicate words should be removed before sorting.
- Sorting should be case-insensitive but the original case should be preserved.
- Use the `sort()` function provided by python.

## Notes:

- Do not remove or rename `sort_sequence(sequence)` function, it's required and should not be altered.
- You can create your own helper functions if needed.
- Ensure the function returns correct outputs for all cases, including edge cases. 
"""


def sort_sequence(sequence):
    pass
