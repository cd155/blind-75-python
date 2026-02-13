"""
Tests for LeetCode 139: Word Break
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("word_break", src_path / "dynamic_programming" / "word_break.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestWordBreak:
    """Test cases for word break problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.wordBreak("leetcode", ["leet", "code"]) == True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.wordBreak("applepenapple", ["apple", "pen"]) == True
