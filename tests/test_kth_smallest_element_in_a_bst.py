"""
Tests for LeetCode 230: Kth Smallest Element in a BST
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("kth_smallest_element_in_a_bst", src_path / "tree" / "kth_smallest_element_in_a_bst.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


class TestKthSmallestElementInBST:
    """Test cases for Kth Smallest Element in a BST problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        assert self.solution.kthSmallest(root, 1) == 1

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
        assert self.solution.kthSmallest(root, 3) == 3

    def test_solution_reusability(self):
        """Test that the same Solution instance can be reused for multiple calls"""
        # First call
        root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        result1 = self.solution.kthSmallest(root1, 1)
        assert result1 == 1
        
        # Second call on the same instance should work correctly
        root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
        result2 = self.solution.kthSmallest(root2, 3)
        assert result2 == 3
        
        # Third call with different k value
        root3 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        result3 = self.solution.kthSmallest(root3, 2)
        assert result3 == 2
