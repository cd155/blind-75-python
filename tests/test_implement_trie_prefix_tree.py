"""
Tests for LeetCode 208: Implement Trie (Prefix Tree)
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("implement_trie_prefix_tree", src_path / "tree" / "implement_trie_prefix_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Trie = module.Trie


class TestImplementTrie:
    """Test cases for Implement Trie problem"""

    def test_example_1(self):
        """Test case from example 1"""
        trie = Trie()
        trie.insert("apple")
        assert trie.search("apple") == True
        assert trie.search("app") == False
        assert trie.startsWith("app") == True
        trie.insert("app")
        assert trie.search("app") == True
