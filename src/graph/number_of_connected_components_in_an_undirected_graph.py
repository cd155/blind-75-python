"""
LeetCode 323: Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi]
indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
"""


class Solution:
    def countComponents(self, n, edges):
        """
        Count connected components in an undirected graph.

        Args:
            n: int - number of nodes
            edges: List[List[int]] - list of edges

        Returns:
            int - number of connected components

        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.countComponents(5, [[0, 1], [1, 2], [3, 4]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
    print(f"Test 2: {result}")
