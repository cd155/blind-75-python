"""
LeetCode 62: Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to
reach the bottom-right corner.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3

Constraints:
- 1 <= m, n <= 100
"""


class Solution:
    def uniquePaths(self, m, n):
        """
        Calculate the number of unique paths in a grid.

        Args:
            m: Number of rows
            n: Number of columns

        Returns:
            Number of unique paths

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.uniquePaths(3, 7)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.uniquePaths(3, 2)
    print(f"Test 2: {result}")
