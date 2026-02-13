"""
LeetCode 297: Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.

        Args:
            root: TreeNode - root of the tree

        Returns:
            str - serialized tree

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement serialize
        pass

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.

        Args:
            data: str - serialized tree

        Returns:
            TreeNode - root of deserialized tree

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement deserialize
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    codec = Codec()

    # Test case 1
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    print(f"Test 1: {deserialized.val if deserialized else None}")

    # Test case 2
    serialized = codec.serialize(None)
    deserialized = codec.deserialize(serialized)
    print(f"Test 2: {deserialized}")
