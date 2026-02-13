"""
Tests for LeetCode 1143: Longest Common Subsequence
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("longest_common_subsequence", src_path / "dynamic_programming" / "longest_common_subsequence.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestLongestCommonSubsequence:
    """Test cases for longest common subsequence problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.longestCommonSubsequence("abcde", "ace") == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.longestCommonSubsequence("abc", "abc") == 3
