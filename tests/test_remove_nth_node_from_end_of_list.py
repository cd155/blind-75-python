"""
Tests for LeetCode 19: Remove Nth Node From End of List
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("remove_nth_node_from_end_of_list", src_path / "linked_list" / "remove_nth_node_from_end_of_list.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
ListNode = module.ListNode


class TestRemoveNthNodeFromEnd:
    """Test cases for Remove Nth Node From End problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = self.solution.removeNthFromEnd(head, 2)
        assert result.val == 1

    def test_example_2(self):
        """Test case from example 2"""
        head = ListNode(1)
        result = self.solution.removeNthFromEnd(head, 1)
        assert result is None
