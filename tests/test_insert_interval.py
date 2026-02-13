"""
Tests for LeetCode 57: Insert Interval
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("insert_interval", src_path / "interval" / "insert_interval.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestInsertInterval:
    """Test cases for Insert Interval problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
