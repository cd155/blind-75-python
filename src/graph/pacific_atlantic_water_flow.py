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
        num_row = len(heights)
        num_column = len(heights[0])
        heights_copy = [[False for _ in range(0, num_column)] for _ in range(0, num_row)]
        path = set()
        pacific_island = set()
        atlantic_island = set()

        def isConnectPacific(i, j, path):
            if (i,j) in pacific_island:
                return True

            if(i,j) in path:
                return False
            path.add((i,j))

            if i == 0 or j == 0:
                pacific_island.add((i,j))
                return True
            
            if i > 0 and heights[i][j] >= heights[i-1][j]:
                if isConnectPacific(i-1, j, path):
                    pacific_island.add((i,j))
                    return True
            if i < num_row-1 and heights[i][j] >= heights[i+1][j]:
                if isConnectPacific(i+1, j, path,):
                    pacific_island.add((i,j))
                    return True
            if j > 0 and heights[i][j] >= heights[i][j-1]:
                if isConnectPacific(i, j-1, path):
                    pacific_island.add((i,j))
                    return True
            if j < num_column-1 and heights[i][j] >= heights[i][j+1]:
                if isConnectPacific(i, j+1, path):
                    pacific_island.add((i,j))
                    return True

            return False

        def isConnectAtlantic(i, j, path):
            if (i,j) in atlantic_island:
                return True
    
            if(i,j) in path:
                return False
            path.add((i,j))
        
            if i == num_row-1 or j == num_column-1:
                atlantic_island.add((i,j))
                return True
            
            if i > 0 and heights[i][j] >= heights[i-1][j]:
                if isConnectAtlantic(i-1, j, path):
                    atlantic_island.add((i,j))
                    return True
            if i < num_row-1 and heights[i][j] >= heights[i+1][j]:
                if isConnectAtlantic(i+1, j, path):
                    atlantic_island.add((i,j))
                    return True
            if j > 0 and heights[i][j] >= heights[i][j-1]:
                if isConnectAtlantic(i, j-1, path):
                    atlantic_island.add((i,j))
                    return True
            if j < num_column-1 and heights[i][j] >= heights[i][j+1]:
                if isConnectAtlantic(i, j+1, path):
                    atlantic_island.add((i,j))
                    return True

            return False

        # can island connect pacific
        for i in range(0, num_row):
            for j in range(0, num_column):
                path.clear()
                if (i,j) in pacific_island or isConnectPacific(i,j,path):
                      heights_copy[i][j] = True 

        # can island connect atlantic
        for i in range(0, num_row):
            for j in range(0, num_column):
                path.clear()
                if ((i,j) in atlantic_island or (isConnectAtlantic(i,j, path))) and heights_copy[i][j]:
                    heights_copy[i][j] = True 
                else:
                    heights_copy[i][j] = False 
        
        good_island = []
        for i in range(0, num_row):
            for j in range(0, num_column):
                if heights_copy[i][j]:
                    good_island.append([i, j])

        return good_island


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.pacificAtlantic([[1]])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.pacificAtlantic([[4,4,4,4], [4,2,2,4], [4,2,2,4], [4,4,4,4]])
    print(f"Test 3: {result}")
