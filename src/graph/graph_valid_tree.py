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
        start_to_end = {}
        for [course_start, course_end] in edges:
            if course_start in start_to_end:
                start_to_end[course_start].append(course_end)
            else:
                start_to_end[course_start] = [course_end]

        vistited = set()

        # Does it have a cycle?
        def dfs(node, path):
            if node in path:
                return True
            path.add(node)

            # reach to end
            if node not in start_to_end:
                return False

            childs = start_to_end[node]
            for child in childs:
                if dfs(child, path):
                    return True

            return False

        for node in range(0, n):
            path = set()
            if dfs(node, path):
                return False

            if not vistited:
                vistited = path
                continue

            if vistited & path:
                vistited = vistited.union(path)
            else:
                return False

        if len(vistited) == n:
            return True

        return False

    def validTree2(self, n, edges):
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
        # Build Undirect Adjacency Node List
        undirect_map = {}
        for [start, end] in edges:
            if start in undirect_map:
                undirect_map[start].append(end)
            else:
                undirect_map[start] = [end]

            if end in undirect_map:
                undirect_map[end].append(start)
            else:
                undirect_map[end] = [start]

        visited = set()

        def dfs(node):
            visited.add(node)
            childs = undirect_map[node]
            for child in childs:
                if child not in visited:
                    dfs(child)

        if len(edges) != n-1:
            return False
        
        dfs(0)

        if len(visited) == n:
            return True

        return False


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.validTree(6, [[5, 4], [4, 3], [3, 2], [1, 2], [0, 4]])
    print(f"Test 3: {result}")
