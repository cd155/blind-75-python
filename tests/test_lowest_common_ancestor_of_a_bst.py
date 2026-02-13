"""
Tests for LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("lowest_common_ancestor_of_a_bst", src_path / "tree" / "lowest_common_ancestor_of_a_bst.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


class TestLowestCommonAncestorOfBST:
    """Test cases for Lowest Common Ancestor of a BST problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
        p = root.left
        q = root.right
        result = self.solution.lowestCommonAncestor(root, p, q)
        assert result.val == 6

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
        p = root.left
        q = root.left.right
        result = self.solution.lowestCommonAncestor(root, p, q)
        assert result.val == 2
