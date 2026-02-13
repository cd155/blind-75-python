"""
Tests for LeetCode 124: Binary Tree Maximum Path Sum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("binary_tree_maximum_path_sum", src_path / "tree" / "binary_tree_maximum_path_sum.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


class TestBinaryTreeMaximumPathSum:
    """Test cases for Binary Tree Maximum Path Sum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert self.solution.maxPathSum(root) == 6

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        assert self.solution.maxPathSum(root) == 42
