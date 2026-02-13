"""
Tests for LeetCode 100: Same Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("same_tree", src_path / "tree" / "same_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


class TestSameTree:
    """Test cases for Same Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        assert self.solution.isSameTree(p, q) == True

    def test_example_2(self):
        """Test case from example 2"""
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        assert self.solution.isSameTree(p, q) == False
