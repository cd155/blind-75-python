"""
Tests for LeetCode 212: Word Search II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("word_search_ii", src_path / "tree" / "word_search_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestWordSearchII:
    """Test cases for Word Search II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        words = ["oath", "pea", "eat", "rain"]
        result = self.solution.findWords(board, words)
        assert sorted(result) == sorted(["eat", "oath"])

    def test_example_2(self):
        """Test case from example 2"""
        board = [["a", "b"], ["c", "d"]]
        words = ["abcb"]
        assert self.solution.findWords(board, words) == []
