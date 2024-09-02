"""
# Generate 2D Array

## Metadata
- Level: 2
- Title: Generate 2D Array
- Topics: List, Iterators

## Instructions
Implement a function called `gen_2d_array(x, y)` which takes `x` and `y` input and
generates a 2-dimensional array. `x` is number or rows and `y` is number of columns.
The element value in the i-th row and j-th column of the array should be i*j.

## Example

Input: (x = 3, y = 5)
Output: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

## How to Test
Run the following command in your terminal:
```bash
python -m unittest tests.test_ex_06
```

## Hints

- Be mindful of edge cases like 0 rows or 0 columns. How should the function behave?
- Consider negative numbers. What happens if `x` or `y` is negative?
- The function should return a 2D list of integers. Handle invalid input by raising a `ValueError`.
- Ensure your function is efficient for large inputs.

## Notes
- Do not remove or rename gen_2d_array(x, y), it's required and should not be altered.
- You can create your own helper functions if needed.
- Ensure the function returns correct outputs for all cases, including edge cases. 
"""


def gen_2d_array(x, y):
    pass
