"""
Tests for LeetCode 191: Number of 1 Bits
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("number_of_1_bits", src_path / "binary" / "number_of_1_bits.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestNumberOf1Bits:
    """Test cases for number of 1 bits problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.hammingWeight(11) == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.hammingWeight(128) == 1
