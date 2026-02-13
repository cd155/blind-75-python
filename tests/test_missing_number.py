"""
Tests for LeetCode 268: Missing Number
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("missing_number", src_path / "binary" / "missing_number.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMissingNumber:
    """Test cases for missing number problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.missingNumber([3, 0, 1]) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.missingNumber([0, 1]) == 2
