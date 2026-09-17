"""
LeetCode 124: Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence
has an edge connecting them. A node can only appear in the sequence at most once. Note that the
path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        """
        Find the maximum path sum in a binary tree.

        Args:
            root: TreeNode - root of the tree

        Returns:
            int - maximum path sum

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    result = solution.maxPathSum(root)
    print(f"Test 1: {result}")

    # Test case 2
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = solution.maxPathSum(root)
    print(f"Test 2: {result}")
