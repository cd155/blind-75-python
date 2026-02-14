"""
LeetCode 102: Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        """
        Perform level order traversal of a binary tree.

        Args:
            root: TreeNode - root of the tree

        Returns:
            List[List[int]] - values by level

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        que = [[root]]
        result = []
        while que:
            nodes = que.pop(0)
            level = []
            new_nodes = []
            for n in nodes:
                if n:
                    level.append(n.val)
                    new_nodes.append(n.left)
                    new_nodes.append(n.right)
            if level:
                result.append(level)
            if new_nodes:
                que.append(new_nodes)
        return result


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = solution.levelOrder(root)
    print(f"Test 1: {result}")

    # Test case 2
    root = TreeNode(1)
    result = solution.levelOrder(root)
    print(f"Test 2: {result}")
