"""
LeetCode 235: Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes
in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow
a node to be a descendant of itself)."

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        Find the lowest common ancestor in a BST.

        Args:
            root: TreeNode - root of the BST
            p: TreeNode - first node
            q: TreeNode - second node

        Returns:
            TreeNode - lowest common ancestor

        Time Complexity: O(h) where h is height
        Space Complexity: O(1) iterative, O(h) recursive
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    p = root.left  # 2
    q = root.right  # 8
    result = solution.lowestCommonAncestor(root, p, q)
    print(f"Test 1: {result.val if result else None}")

    # Test case 2
    p = root.left  # 2
    q = root.left.right  # 4
    result = solution.lowestCommonAncestor(root, p, q)
    print(f"Test 2: {result.val if result else None}")
