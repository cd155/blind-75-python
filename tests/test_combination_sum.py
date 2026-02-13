"""
Tests for LeetCode 39: Combination Sum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("combination_sum", src_path / "dynamic_programming" / "combination_sum.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCombinationSum:
    """Test cases for combination sum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
