"""
Tests for LeetCode 206: Reverse Linked List
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("reverse_linked_list", src_path / "linked_list" / "reverse_linked_list.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
ListNode = module.ListNode


class TestReverseLinkedList:
    """Test cases for Reverse Linked List problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = self.solution.reverseList(head)
        assert result.val == 5

    def test_example_2(self):
        """Test case from example 2"""
        head = ListNode(1, ListNode(2))
        result = self.solution.reverseList(head)
        assert result.val == 2
