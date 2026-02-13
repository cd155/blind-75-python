"""
Tests for LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("construct_binary_tree_from_preorder_and_inorder_traversal", src_path / "tree" / "construct_binary_tree_from_preorder_and_inorder_traversal.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestConstructBinaryTree:
    """Test cases for Construct Binary Tree from Preorder and Inorder Traversal problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        assert result.val == 3

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.buildTree([-1], [-1])
        assert result.val == -1
