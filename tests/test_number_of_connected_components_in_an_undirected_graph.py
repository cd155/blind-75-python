"""
Tests for LeetCode 323: Number of Connected Components in an Undirected Graph
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("number_of_connected_components_in_an_undirected_graph", src_path / "graph" / "number_of_connected_components_in_an_undirected_graph.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestNumberOfConnectedComponents:
    """Test cases for Number of Connected Components problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
