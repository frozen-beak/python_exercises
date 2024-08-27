"""
# Dictionary of Squares

## Metadata
- Level: 1
- Title: Dictionary of Squares
- Topics: Loop, Dictionary, Error Handling

## Instructions
Write a function called `get_squares(n)` that generates a dictionary that contains (i, i*i)
such that `i` is an integer between [1] and [n] (both included). The function then should return
this dictionary as an output.

## Example

Input: 6
Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

## How to Test
Run the following command in your terminal:
```bash
python -m unittest tests.test_ex_04
```

## Hints
- Raise a value error if `n` is not a positive integer
- Use python dictionary to store output
- Use the `range` function to iterate till `n`, don't forget to include `n`
- 0 is not a positive integer

## Notes
- Do not remove or rename `get_squares(n)`, it's required and should not be altered.
- You can create your own helper functions if needed.
- Make sure your implementation can handle large inputs efficiently.
"""


def get_squares(n):

    if not isinstance(n, int) or n < 1:
        raise ValueError("N should only be a positive integer")

    squares = {}

    for i in range(1, n + 1):
        squares[i] = i * i

    return squares
