"""
Tests for LeetCode 152: Maximum Product Subarray
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("maximum_product_subarray", src_path / "array" / "maximum_product_subarray.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMaximumProductSubarray:
    """Test cases for maximum product subarray problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.maxProduct([2, 3, -2, 4]) == 6

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.maxProduct([-2, 0, -1]) == 0

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.maxProduct([-4, -3, -2]) == 12
