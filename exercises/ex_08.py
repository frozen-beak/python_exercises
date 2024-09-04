"""
# Transpose Matrix

## Metadata
- Level: 2
- Title: Transpose Matrix
- Topics: List, Matrix Manipulation, Iterators

## Instructions
Implement a function `transpose_matrix(matrix)` that takes a 2-dimensional array (matrix)
and returns its transpose. 

## What is Transpose of a Matrix

The transpose of a matrix is a new matrix that is obtained by swapping the rows and columns 
of the original matrix. In the transposed matrix, the element at position `(i, j)` in the 
original matrix will be at position `(j, i)` in the transposed matrix.

Example:

Original Matrix:

1  2  3
4  5  6

Transpose:

1  4
2  5
3  6

## Example

Input: [[1, 2, 3], [4, 5, 6]]
Output: [[1, 4], [2, 5], [3, 6]]

## How to Test

Run the following command in your terminal:
```bash
python -m unittest tests.test_ex_08
```

## Hints

- Handle edge cases like an empty matrix, or matrices with only one row or column.
- Ensure that all rows have the same number of columns (rectangular matrix) before transposing.
- Raise a `ValueError` for invalid inputs such as non-rectangular matrices or non-numeric data.

## Notes

- Do not remove or rename `transpose_matrix(matrix)`.
- You can create helper functions if needed
- Ensure correct behavior for edge cases and invalid inputs. 
"""


def transpose_matrix(matrix):
    pass
