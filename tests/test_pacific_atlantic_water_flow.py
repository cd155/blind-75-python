"""
Tests for LeetCode 417: Pacific Atlantic Water Flow
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("pacific_atlantic_water_flow", src_path / "graph" / "pacific_atlantic_water_flow.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestPacificAtlanticWaterFlow:
    """Test cases for Pacific Atlantic Water Flow problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
        result = self.solution.pacificAtlantic(heights)
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        assert sorted(result) == sorted(expected)

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.pacificAtlantic([[1]]) == [[0, 0]]
