"""
LeetCode 200: Number of Islands

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

Example 1:
Input: grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
Output: 1

Example 2:
Input: grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'
"""


class Solution:
    def numIslands(self, grid):
        """
        Count the number of islands in a grid.

        Args:
            grid: List[List[str]] - 2D grid of '0' and '1'

        Returns:
            int - number of islands

        Time Complexity: O(m * n)
        Space Complexity: O(m * n) for recursion stack
        """
        if not grid or not grid[0]:
            return 0

        row_num = len(grid)
        col_num = len(grid[0])
        visit_record = set()
        num_island = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if (i,j) not in visit_record and grid[i][j] == "1":
                visit_record.add((i, j))
                for di, dj in directions:
                    next_i, next_j = i + di, j + dj
                    if 0 <= next_i < row_num and 0 <= next_j < col_num:
                        dfs(next_i, next_j)

        for i in range(0, row_num):
            for j in range(0, col_num):
                if (i,j) not in visit_record and grid[i][j] == "1":
                    num_island += 1
                    dfs(i, j)

        return num_island


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
    print(f"Test 2: {result}")
