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
    def get_undirected_node_map(self, edges):
        undirected_node_map = {}
        for [start, end] in edges:
            if start in undirected_node_map:
                undirected_node_map[start].append(end)
            else:
                undirected_node_map[start] = [end]

            if end in undirected_node_map:
                undirected_node_map[end].append(start)
            else:
                undirected_node_map[end] = [start]
        return undirected_node_map

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
        # Build Undirect Adjacency Node List
        undirected_node_map = self.get_undirected_node_map(edges)
        visited = set()

        def dfs(node):
            visited.add(node)
            childs = undirected_node_map.get(node, [])
            for child in childs:
                if child not in visited:
                    dfs(child)

        # a tree need to have n-1 edges
        if len(edges) != n-1:
            return False
        
        dfs(0)

        if len(visited) == n:
            return True

        return False

    def valid_tree_parent_pointer(self, n, edges):
        # Build Undirect Adjacency Node List
        undirected_node_map = self.get_undirected_node_map(edges)
        visited = set()

        # Does it have a cycle with parent pointer?
        def dfs(node, parent):
            if node in visited:
                return True
            visited.add(node)

            # reach to end
            if node not in undirected_node_map:
                return False

            childs = undirected_node_map[node]
            for child in childs:
                if child != parent: 
                    if dfs(child, node):
                        return True

            return False

        if dfs(0, None):
            return False

        if len(visited) == n:
            return True

        return False

    def valid_tree_union_find(self, n, edges):
        parent = [i for i in range(n)]
        # number of nodes join
        count = [0]

        def find(x):
            if x != parent[x]:
                x = find(parent[x])
            return x

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                parent[root_y] = root_x
                count[0] += 1
                return False
            else:
                return True

        for s, e in edges:
            is_cycle = union(s, e)
            if is_cycle:
                return False
        
        num_of_nodes = count[0] + 1
        if num_of_nodes != n:
            return False

        return True


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.valid_tree_union_find(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.valid_tree_union_find(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.valid_tree_union_find(6, [[5, 4], [4, 3], [3, 2], [1, 2], [0, 4]])
    print(f"Test 3: {result}")
