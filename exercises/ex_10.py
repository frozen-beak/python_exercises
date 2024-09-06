"""
# Binary Divisibility by 5

## Metadata
- Level: 2
- Title: Binary Divisibility by 5
- Topics: Binary Numbers, Modulus, Input Validation

## Instructions
Write a function `is_binary_divisible_by_5(binary_str)` that takes a string `binary_str`, which
represents a binary number, and returns `True` if the number is divisible by 5, and `False` otherwise.
The function should raise a `ValueError` if the input is not a valid binary number.

## Example

Input: "1001"  (which is 9 in decimal)
Output: False

Input: "10100" (which is 20 in decimal)
Output: True

## How to Test

Run the following command in your terminal:
```bash
python -m unittest tests.test_ex_10
```

## What is Binary Divisibility?

A binary number can be converted into its decimal form by multiplying each digit by powers of 2.
Once the binary number is converted to decimal, it can be checked if it is divisible by 5 
using the modulus operator `%`.

## Example

Input: "10100"
Output: True
Logic: "10100" is `20` in base10 and `20 % 5 == 0`

## Hints

- Use the built-in `int()` function to convert a binary string to a decimal number.
- Ensure the input is a valid binary string consisting of only '0' and '1'.
- Handle cases where the input is empty or contains invalid characters.

## Notes

- Do not remove or rename `is_binary_divisible_by_5(binary_str)`.
- You can create helper functions if needed.
"""


def is_binary_divisible_by_5(binary_str):
    pass
