"""
LeetCode 48: Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000
"""


class Solution:
    def rotate(self, matrix):
        """
        Rotate matrix 90 degrees clockwise in-place.

        Args:
            matrix: List[List[int]] - n x n matrix

        Returns:
            None - modifies matrix in-place

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(matrix)

        new_matrix = []
        for _ in range(n):
            new_matrix.append([0]*n)

        # rotate in new image
        for r in range(n):
            for c in range(n):
                new_matrix[c][(n-1)-r] = matrix[r][c]

        return new_matrix

    def rotate_in_place_cal(self, matrix):
        n = len(matrix)
        for r in range(n//2):
            for c in range(r, n-r-1):
                rotate_count = 0
                next_r, next_c = r, c
                store_pre = matrix[next_r][next_c]

                while rotate_count < 4:
                    next_r, next_c = next_c, (n-1)-next_r
                    temp = matrix[next_r][next_c]
                    matrix[next_r][next_c] = store_pre
                    store_pre = temp
                    rotate_count += 1
        return matrix

    def rotate_in_place_swap(self, matrix):
        n = len(matrix)
        for r in range(n//2):
            for c in range(r, n-r-1):
                (
                    matrix[c][n-1-r],
                    matrix[n-1-r][n-1-c],
                    matrix[n-1-c][r],
                    matrix[r][c],
                ) = (
                    matrix[r][c],
                    matrix[c][n-1-r],
                    matrix[n-1-r][n-1-c],
                    matrix[n-1-c][r],
                )
        return matrix

    def pretty_print(self, matrix):
        for row in matrix:
            print(row)


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    matrix = [[1, 2], [3, 4]]
    new_matrix = solution.rotate_in_place_swap(matrix)
    print(f"Test 1:")
    solution.pretty_print(new_matrix)

    # Test case 2
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    new_matrix = solution.rotate_in_place_swap(matrix)
    print(f"Test 2:")
    solution.pretty_print(new_matrix)

    # Test case 3
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    new_matrix = solution.rotate_in_place_swap(matrix)
    print(f"Test 3:")
    solution.pretty_print(new_matrix)