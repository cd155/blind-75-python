"""
Tests for LeetCode 252: Meeting Rooms
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("meeting_rooms", src_path / "interval" / "meeting_rooms.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMeetingRooms:
    """Test cases for Meeting Rooms problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) == False

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.canAttendMeetings([[7, 10], [2, 4]]) == True
