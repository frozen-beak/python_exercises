"""
# Matrix Multiplication

## Metadata
- Level: 3
- Title: Matrix Multiplication
- Topics: List, Matrix Manipulation, Iterators, Nested Loops

## Instructions
Implement a function `multiply_matrices(matrix1, matrix2)` that multiplies two matrices.
Matrix multiplication is only possible when the number of columns in `matrix1` is equal to
the number of rows in `matrix2`. The result of the multiplication will be a new matrix where each
element is the sum of the products of the corresponding row from `matrix1` and the column from `matrix2`.

## Example

Input:
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

Output:
[[19, 22], [43, 50]]

## How to Test

Run the following command in your terminal:
```bash
python -m unittest tests.test_ex_09
```


## What is Matrix Multiplication?

Matrix multiplication is the process of multiplying two matrices by taking the dot product
of rows and columns. If `matrix1` is of size `m x n` and `matrix2` is of size `n x p`,
the resulting matrix will have size `m x p`. Each element in the result is the sum of products
of corresponding elements in the row from `matrix1` and the column from `matrix2`.

## Example

Matrix 1:

```
1  2
3  4
```

Matrix 2:

```
5  6
7  8
```

Multiplication:

```
(1*5 + 2*7)  (1*6 + 2*8)
(3*5 + 4*7)  (3*6 + 4*8)
```

Result:

```
19  22
43  50
```

## Hints

- Ensure that the number of columns in `matrix1` is equal to the number of rows in `matrix2`.
- Use nested loops or list comprehensions to perform the matrix multiplication.
- Raise a `ValueError` for invalid input or when matrix multiplication is not possible.

## Notes

- Do not remove or rename `multiply_matrices(matrix1, matrix2)`.
- You can create helper functions if needed.
- Ensure that the function works efficiently for larger matrices.
"""


def multiply_matrices(matrix1, matrix2):
    pass
