"""
Tests for LeetCode 21: Merge Two Sorted Lists
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("merge_two_sorted_lists", src_path / "linked_list" / "merge_two_sorted_lists.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
ListNode = module.ListNode


class TestMergeTwoSortedLists:
    """Test cases for Merge Two Sorted Lists problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        result = self.solution.mergeTwoLists(list1, list2)
        assert result.val == 1

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.mergeTwoLists(None, None)
        assert result is None
