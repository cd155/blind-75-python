"""
LeetCode 73: Set Matrix Zeroes

Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1
"""


class Solution:
    def setZeroes(self, matrix):
        """
        Set entire row and column to 0 if element is 0.

        Args:
            matrix: List[List[int]] - input matrix

        Returns:
            None - modifies matrix in-place

        Time Complexity: O(m * n)
        Space Complexity: O(1)
        """
        row_zeros = set()
        col_zeros = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zeros.add(i)
                    col_zeros.add(j)

        for row in row_zeros:
            for j in range(n):
                matrix[row][j] = 0

        for col in col_zeros:
            for i in range(m):
                matrix[i][col] = 0

        return matrix

    def set_zeros_space_one(self, matrix):
        m, n = len(matrix), len(matrix[0])
        is_first_row_zero = False
        is_first_col_zero = False

        for i in range(0, m):
            if matrix[i][0] == 0:
                is_first_col_zero = True
                break

        for j in range(0, n):
            if matrix[0][j] == 0:
                is_first_row_zero = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if is_first_col_zero:
            for i in range(0, m):
                matrix[i][0] = 0

        if is_first_row_zero:
            for j in range(0, n):
                matrix[0][j] = 0

        return matrix


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution.setZeroes(matrix)
    print(f"Test 1: {matrix}")

    # Test case 2
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution.setZeroes(matrix)
    print(f"Test 2: {matrix}")
