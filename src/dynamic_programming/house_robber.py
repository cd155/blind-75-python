"""
LeetCode 198: House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount
of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses
have security systems connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount
of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400
"""


class Solution:
    def rob(self, nums):
        """
        Find the maximum amount that can be robbed without alerting police.

        Args:
            nums: List of money amounts in each house

        Returns:
            Maximum amount that can be robbed

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.rob([1, 2, 3, 1])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.rob([2, 7, 9, 3, 1])
    print(f"Test 2: {result}")
