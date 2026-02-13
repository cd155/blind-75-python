"""
Tests for LeetCode 198: House Robber
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("house_robber", src_path / "dynamic_programming" / "house_robber.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestHouseRobber:
    """Test cases for house robber problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.rob([1, 2, 3, 1]) == 4

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.rob([2, 7, 9, 3, 1]) == 12
