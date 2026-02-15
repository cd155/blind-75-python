"""
LeetCode 98: Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        """
        Validate if a binary tree is a valid BST.

        Args:
            root: TreeNode - root of the tree

        Returns:
            bool - true if valid BST

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        bst = self.treeToArray(root)
        if not bst:
            return True
        
        for i in range(1,len(bst)):
            if bst[i-1] > bst[i]:
                return False
        return True

    def treeToArray(self, root):
        if root is None:
            return []
        return self.treeToArray(root.left) + \
               [root.val] + \
               self.treeToArray(root.right)
    
    def treeToArrayAlter(self, root):
        bst_array = []

        def traverse(node):
            if node is None:
                return            
            traverse(node.left)
            bst_array.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return bst_array

    def isValidBSTBetter(self, root):

        def validate(root, low, high):
            if root is None:
                return True
            if root.val <= low or root.val >= high:
                return False

            # go left and go right
            return validate(root.left, low, root.val) and \
                   validate(root.right, root.val, high)            

        return validate(root, float('-inf'), float('inf'))


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    result = solution.isValidBSTBetter(root)
    print(f"Test 1: {result}")

    # Test case 2
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    result = solution.isValidBSTBetter(root)
    print(f"Test 2: {result}")
