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
    def pacificAtlanticDownhill(self, heights):
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
        path = set()
        pacific_island_success = set()
        atlantic_island_success = set()
        pacific_island_fail = set()
        atlantic_island_fail = set()

        def isConnectPacific(i, j, path):
            if (i,j) in pacific_island_success:
                return True
            
            if (i,j) in pacific_island_fail:
                return False

            if(i,j) in path:
                return False
            path.add((i,j))

            if i == 0 or j == 0:
                pacific_island_success.add((i,j))
                return True
            
            hit_cycle = False
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for (di, dj) in directions:
                next_i, next_j = i+di, j+dj
                if (0 <= next_i < num_row and 
                    0 <= next_j < num_column and
                    heights[i][j] >= heights[next_i][next_j]):

                    if(next_i, next_j) in path:
                        hit_cycle = True
                        continue

                    if(isConnectPacific(next_i, next_j,path)):
                        pacific_island_success.add((i,j))
                        return True

            if not hit_cycle:
                pacific_island_fail.add((i, j))
            return False

        def isConnectAtlantic(i, j, path):
            if (i,j) in atlantic_island_success:
                return True
            
            if (i,j) in atlantic_island_fail:
                return False

            if(i,j) in path:
                return False
            path.add((i,j))
        
            if i == num_row-1 or j == num_column-1:
                atlantic_island_success.add((i,j))
                return True
            
            direction = [(-1,0), (1,0), (0,-1), (0,1)]
            hit_cycle = False
            for (di, dj) in direction:
                next_i, next_j = i+di, j+dj
            
                if(0 <= next_i < num_row and
                   0 <= next_j < num_column and 
                   heights[i][j] >= heights[next_i][next_j]):
                    
                    if (next_i,next_j) in path:
                        hit_cycle = True
                        continue

                    if isConnectAtlantic(next_i, next_j, path):
                        atlantic_island_success.add((i,j))
                        return True
            if not hit_cycle:
                atlantic_island_fail.add((i,j))
            return False
        
        good_island = []
        for i in range(0, num_row):
            for j in range(0, num_column):
                path.clear()
                reach_pacific = (i,j) in pacific_island_success or isConnectPacific(i,j,path)

                path.clear()
                reach_atlantic = (i,j) in atlantic_island_success or isConnectAtlantic(i,j, path)
                
                if reach_pacific and reach_atlantic:
                    good_island.append([i, j])

        return good_island


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.pacificAtlanticDownhill([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.pacificAtlanticDownhill([[1]])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.pacificAtlanticDownhill([[4,4,4,4], [4,2,2,4], [4,2,2,4], [4,4,4,4]])
    print(f"Test 3: {result}")
