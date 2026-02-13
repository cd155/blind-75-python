"""
Tests for LeetCode 56: Merge Intervals
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("merge_intervals", src_path / "interval" / "merge_intervals.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMergeIntervals:
    """Test cases for Merge Intervals problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
