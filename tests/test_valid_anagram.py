"""
Tests for LeetCode 242: Valid Anagram
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("valid_anagram", src_path / "string" / "valid_anagram.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestValidAnagram:
    """Test cases for Valid Anagram problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.isAnagram("anagram", "nagaram") == True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.isAnagram("rat", "car") == False
