"""
Tests for LeetCode 5: Longest Palindromic Substring
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("longest_palindromic_substring", src_path / "string" / "longest_palindromic_substring.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestLongestPalindromicSubstring:
    """Test cases for Longest Palindromic Substring problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.longestPalindrome("babad")
        assert result in ["bab", "aba"]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.longestPalindrome("cbbd") == "bb"
