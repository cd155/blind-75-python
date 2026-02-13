"""
LeetCode 417: Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the
island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix
heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[1]]
Output: [[0,0]]

Constraints:
- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
"""


class Solution:
    def pacificAtlantic(self, heights):
        """
        Find cells where water can flow to both oceans.

        Args:
            heights: List[List[int]] - height matrix

        Returns:
            List[List[int]] - coordinates of cells

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.pacificAtlantic([[1]])
    print(f"Test 2: {result}")
