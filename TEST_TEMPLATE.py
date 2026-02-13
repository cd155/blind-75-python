"""
Tests for LeetCode {NUMBER}: {TITLE}
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from {category}.{filename} import Solution


class Test{ClassName}:
    """Test cases for {problem_name} problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.{method_name}({TEST_INPUT_1}) == {EXPECTED_OUTPUT_1}

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.{method_name}({TEST_INPUT_2}) == {EXPECTED_OUTPUT_2}
