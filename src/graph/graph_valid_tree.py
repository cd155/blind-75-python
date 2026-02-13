"""
LeetCode 261: Graph Valid Tree

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of
edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
"""


class Solution:
    def validTree(self, n, edges):
        """
        Check if graph forms a valid tree.

        Args:
            n: int - number of nodes
            edges: List[List[int]] - list of edges

        Returns:
            bool - true if graph is a valid tree

        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    print(f"Test 2: {result}")
