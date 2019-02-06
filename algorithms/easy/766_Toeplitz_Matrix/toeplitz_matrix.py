#! /usr/bin/env python
"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

    matrix will be a 2D array of integers.
    matrix will have a number of rows and columns in range [1, 20].
    matrix[i][j] will be integers in range [0, 99].
"""
import unittest


def isToeplitzMatrix(matrix: "List[List[int]]") -> "bool":
    return all(
        r == 0 or c == 0 or matrix[r - 1][c - 1] == val
        for r, row in enumerate(matrix)
        for c, val in enumerate(row)
    )


class TestSolution(unittest.TestCase):
    def test_example(self):
        matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
        ans = isToeplitzMatrix(matrix)
        self.assertTrue(ans)


if __name__ == "__main__":
    unittest.main()
