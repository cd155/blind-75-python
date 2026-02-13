"""
LeetCode 322: Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be
made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""


class Solution:
    def coinChange(self, coins, amount):
        """
        Find the minimum number of coins needed to make the amount.

        Args:
            coins: List of coin denominations
            amount: Target amount

        Returns:
            Minimum number of coins, or -1 if impossible

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.coinChange([1, 2, 5], 11)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.coinChange([2], 3)
    print(f"Test 2: {result}")
