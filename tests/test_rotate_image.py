"""
Tests for LeetCode 48: Rotate Image
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("rotate_image", src_path / "matrix" / "rotate_image.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestRotateImage:
    """Test cases for Rotate Image problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.solution.rotate(matrix)
        assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    def test_example_2(self):
        """Test case from example 2"""
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        self.solution.rotate(matrix)
        assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
