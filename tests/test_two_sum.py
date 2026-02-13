"""
Tests for LeetCode 1: Two Sum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("two_sum", src_path / "array" / "two_sum.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestTwoSum:
    """Test cases for two sum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.twoSum([2, 7, 11, 15], 9) == [0, 1]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.twoSum([3, 2, 4], 6) == [1, 2]
