"""
Tests for LeetCode 11: Container With Most Water
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("container_with_most_water", src_path / "array" / "container_with_most_water.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestContainerWithMostWater:
    """Test cases for container with most water problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.maxArea([1, 1]) == 1
