"""
LeetCode 226: Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        """
        Invert a binary tree.

        Args:
            root: TreeNode - root of the tree

        Returns:
            TreeNode - root of inverted tree

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if root is None:
            return

        buffer = root.left
        root.left = root.right
        root.right = buffer

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def pretty_print_node(self, root):
        if root is None:
            return
        print(root.val)
        self.pretty_print_node(root.left)
        self.pretty_print_node(root.right)


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    result = solution.invertTree(root)
    solution.pretty_print_node(result)

    # Test case 2
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    result = solution.invertTree(root)
    solution.pretty_print_node(result)
