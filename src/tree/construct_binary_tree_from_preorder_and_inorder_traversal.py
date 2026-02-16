"""
LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a
binary tree and inorder is the inorder traversal of the same tree, construct and return the
binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        """
        Build binary tree from preorder and inorder traversals.

        Args:
            preorder: List[int] - preorder traversal
            inorder: List[int] - inorder traversal

        Returns:
            TreeNode - root of constructed tree

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        self.pre_index = 0

        in_val_to_index = {}
        for i, val in enumerate(inorder):
            in_val_to_index[val] = i

        def dfs_build(inorder_arr, l, h):
            if l>=h:
                return None
            node_val = preorder[self.pre_index]
            node = TreeNode(node_val)
            self.pre_index += 1
            node.left = dfs_build (inorder_arr, l, in_val_to_index[node_val])
            node.right = dfs_build (inorder_arr, in_val_to_index[node_val]+1, h)
            return node

        return dfs_build(inorder, 0, len(preorder))


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(f"Test 1: {result.val if result else None}")

    # Test case 2
    result = solution.buildTree([-1], [-1])
    print(f"Test 2: {result.val if result else None}")
