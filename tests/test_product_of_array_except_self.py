"""
Tests for LeetCode 238: Product of Array Except Self
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("product_of_array_except_self", src_path / "array" / "product_of_array_except_self.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestProductOfArrayExceptSelf:
    """Test cases for product of array except self problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
