"""
Tests for LeetCode 253: Meeting Rooms II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("meeting_rooms_ii", src_path / "interval" / "meeting_rooms_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMeetingRoomsII:
    """Test cases for Meeting Rooms II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.minMeetingRooms([[7, 10], [2, 4]]) == 1
