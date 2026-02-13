"""
Tests for LeetCode 371: Sum of Two Integers
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("sum_of_two_integers", src_path / "binary" / "sum_of_two_integers.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSumOfTwoIntegers:
    """Test cases for sum of two integers problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.getSum(1, 2) == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.getSum(2, 3) == 5
