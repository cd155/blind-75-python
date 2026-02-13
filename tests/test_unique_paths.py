"""
Tests for LeetCode 62: Unique Paths
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("unique_paths", src_path / "dynamic_programming" / "unique_paths.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestUniquePaths:
    """Test cases for unique paths problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.uniquePaths(3, 7) == 28

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.uniquePaths(3, 2) == 3
