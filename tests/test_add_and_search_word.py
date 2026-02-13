"""
Tests for LeetCode 211: Design Add and Search Words Data Structure
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("add_and_search_word", src_path / "tree" / "add_and_search_word.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
WordDictionary = module.WordDictionary


class TestAddAndSearchWord:
    """Test cases for Add and Search Word problem"""

    def test_example_1(self):
        """Test case from example 1"""
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        assert wordDictionary.search("pad") == False
        assert wordDictionary.search("bad") == True
        assert wordDictionary.search(".ad") == True
        assert wordDictionary.search("b..") == True
