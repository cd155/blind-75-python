"""
LeetCode 572: Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root
with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree is a tree that consists of a node in tree and all of this node's
descendants. The tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -10^4 <= root.val <= 10^4
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root, subRoot):
        """
        Check if subRoot is a subtree of root.

        Args:
            root: TreeNode - root of the main tree
            subRoot: TreeNode - root of the potential subtree

        Returns:
            bool - true if subRoot is a subtree

        Time Complexity: O(m * n) where m, n are tree sizes
        Space Complexity: O(h)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    result = solution.isSubtree(root, subRoot)
    print(f"Test 1: {result}")

    # Test case 2
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    result = solution.isSubtree(root, subRoot)
    print(f"Test 2: {result}")
