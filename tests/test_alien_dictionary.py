"""
Tests for LeetCode 269: Alien Dictionary
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("alien_dictionary", src_path / "graph" / "alien_dictionary.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestAlienDictionary:
    """Test cases for Alien Dictionary problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
        assert result == "wertf"

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.alienOrder(["z", "x"])
        assert result == "zx"
