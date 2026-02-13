"""
Tests for LeetCode 141: Linked List Cycle
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("linked_list_cycle", src_path / "linked_list" / "linked_list_cycle.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
ListNode = module.ListNode


class TestLinkedListCycle:
    """Test cases for Linked List Cycle problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1 - with cycle"""
        head = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        assert self.solution.hasCycle(head) == True

    def test_example_2(self):
        """Test case from example 2 - no cycle"""
        head = ListNode(1, ListNode(2))
        assert self.solution.hasCycle(head) == False
