"""
LeetCode 133: Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Example 2:
Input: adjList = [[]]
Output: [[]]

Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        """
        Clone an undirected graph.

        Args:
            node: Node - reference to a node in the graph

        Returns:
            Node - cloned graph

        Time Complexity: O(N + E) where N is number of nodes and E is edges
        Space Complexity: O(N) for the hashmap
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    result = solution.cloneGraph(node1)
    print(f"Test 1: Cloned graph starting at node {result.val if result else None}")

    # Test case 2
    result = solution.cloneGraph(None)
    print(f"Test 2: {result}")
