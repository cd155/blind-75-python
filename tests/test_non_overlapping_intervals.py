"""
Tests for LeetCode 435: Non-overlapping Intervals
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("non_overlapping_intervals", src_path / "interval" / "non_overlapping_intervals.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestNonOverlappingIntervals:
    """Test cases for Non-overlapping Intervals problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
