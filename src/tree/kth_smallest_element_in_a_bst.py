"""
LeetCode 230: Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value
(1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        """
        Find the kth smallest element in a BST.

        Args:
            root: TreeNode - root of the BST
            k: int - the k value (1-indexed)

        Returns:
            int - kth smallest value

        Time Complexity: O(h + k) where h is height
        Space Complexity: O(h)
        """
        def traverse(root):
            if root is None:
                return

            left_result = traverse(root.left)            
            # Check "is not None" so that 0 is accepted as a valid answer            
            if left_result is not None:
                return left_result

            self.k -= 1
            if self.k == 0:            
                return root.val

            return traverse(root.right)            

        return traverse(root)

# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    result = solution.kthSmallest(root, 1)
    print(f"Test 1: {result}")

    # Test case 2
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    result = solution.kthSmallest(root, 3)
    print(f"Test 2: {result}")
