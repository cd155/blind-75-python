"""
Tests for LeetCode 121: Best Time to Buy and Sell Stock
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("best_time_to_buy_and_sell_stock", src_path / "array" / "best_time_to_buy_and_sell_stock.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestBestTimeToBuyAndSellStock:
    """Test cases for best time to buy and sell stock problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.maxProfit([7, 6, 4, 3, 1]) == 0
