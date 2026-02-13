"""
Tests for LeetCode 190: Reverse Bits
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("reverse_bits", src_path / "binary" / "reverse_bits.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestReverseBits:
    """Test cases for reverse bits problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.reverseBits(0b00000010100101000001111010011100) == 964176192

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.reverseBits(0b11111111111111111111111111111101) == 3221225471
