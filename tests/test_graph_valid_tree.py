"""
Tests for LeetCode 261: Graph Valid Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("graph_valid_tree", src_path / "graph" / "graph_valid_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestGraphValidTree:
    """Test cases for Graph Valid Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False
