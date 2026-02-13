"""
Tests for LeetCode 153: Find Minimum in Rotated Sorted Array
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("find_minimum_in_rotated_sorted_array", src_path / "array" / "find_minimum_in_rotated_sorted_array.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestFindMinimumInRotatedSortedArray:
    """Test cases for find minimum in rotated sorted array problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.findMin([3, 4, 5, 1, 2]) == 1

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
