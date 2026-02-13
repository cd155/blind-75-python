"""
LeetCode 104: Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        """
        Find the maximum depth of a binary tree.

        Args:
            root: TreeNode - root of the tree

        Returns:
            int - maximum depth

        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = solution.maxDepth(root)
    print(f"Test 1: {result}")

    # Test case 2
    root = TreeNode(1, None, TreeNode(2))
    result = solution.maxDepth(root)
    print(f"Test 2: {result}")
