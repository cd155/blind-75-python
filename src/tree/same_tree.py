"""
LeetCode 100: Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have
the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        """
        Check if two binary trees are identical.

        Args:
            p: TreeNode - root of first tree
            q: TreeNode - root of second tree

        Returns:
            bool - true if trees are same

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    result = solution.isSameTree(p, q)
    print(f"Test 1: {result}")

    # Test case 2
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    result = solution.isSameTree(p, q)
    print(f"Test 2: {result}")
