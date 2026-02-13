"""
Tests for LeetCode 226: Invert Binary Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("invert_binary_tree", src_path / "tree" / "invert_binary_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


class TestInvertBinaryTree:
    """Test cases for Invert Binary Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
        result = self.solution.invertTree(root)
        assert result.val == 4
        assert result.left.val == 7
        assert result.right.val == 2

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        result = self.solution.invertTree(root)
        assert result.val == 2
