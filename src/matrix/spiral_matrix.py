"""
LeetCode 54: Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        Return matrix elements in spiral order.

        Args:
            matrix: List[List[int]] - input matrix

        Returns:
            List[int] - elements in spiral order

        Time Complexity: O(m * n)
        Space Complexity: O(1) excluding output
        """
        row_size, col_size = len(matrix), len(matrix[0])
        start_row, end_row = 0, row_size-1
        start_col, end_col = 0, col_size-1
        result = []
        while end_row >= start_row and end_col >= start_col:            

            # step 1
            for j in range(start_col, end_col+1):
                result.append(matrix[start_row][j])
            start_row += 1
            
            # step 2
            for i in range(start_row, end_row+1):
                result.append(matrix[i][end_col])
            end_col -= 1

            if start_row > end_row or start_col > end_col: break
            
            # step 3
            for j in reversed(range(start_col, end_col+1)):
                print(start_col, end_col+1)

                result.append(matrix[end_row][j])
            end_row -= 1

            # step 4
            for i in reversed(range(start_row, end_row+1)):
                result.append(matrix[i][start_col])
            start_col += 1

        return result


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.spiralOrder([[1, 2]])
    print(f"Test 3: {result}")