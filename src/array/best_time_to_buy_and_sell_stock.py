"""
LeetCode 121: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""


class Solution:
    def maxProfit(self, prices):
        """
        Find the maximum profit from buying and selling stock once.

        Args:
            prices: List of stock prices

        Returns:
            Maximum profit

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        lowest, m_p = prices[0], 0
        for p in prices[1:]:
            if p < lowest:
                lowest = p
            else:
                m_p = max(m_p, p-lowest)
        return m_p


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.maxProfit([7, 1, 5, 3, 6, 4])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.maxProfit([7, 6, 4, 3, 1])
    print(f"Test 2: {result}")
