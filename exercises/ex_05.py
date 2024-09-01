"""
# Implement EOQ (Economic Order Quantity) Formula

## Metadata
- Level: 2
- Title: Implement EOQ Formula
- Topics: Arithmetics, Error Handling 

## Instructions
Implement a function `calculate_eoq(d)` which calculate values of `q` according to EOQ
formula. Formula to calculate EOQ is, `Q = Square root of [(2 * C * D)/H]`, where C and H
are constants with 50 & 30 as values respectively. D is provided as input and Q is to be
calculated and return as a _result_.

## Example

Input: 180
Output: 24

## How to Test
Run the following command in your terminal:
```bash
python -m unittest tests.test_ex_05
```

## Hints

- If the calculated output is in decimal form, it should be rounded off to its nearest integer
  (ex, if calculated output is `26.0` then it should be `26`)
- Raise `ValueError` if `D` is not a integer
- Use `math` module provided by python for arithmetic operations

## Notes
- Do not remove or rename `calculate_eoq(d)`, it's required and should not be altered.
- You can create your own helper functions if needed.
- Make sure your checking for invalid inputs correctly and raising errors if required.
"""


def calculate_eoq(D):
    pass
