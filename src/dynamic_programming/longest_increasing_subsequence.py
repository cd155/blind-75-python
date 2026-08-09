"""
LeetCode 300: Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def lengthOfLIS(self, nums):
        """
        Find the length of the longest increasing subsequence.

        Args:
            nums: List of integers

        Returns:
            Length of longest increasing subsequence

        Time Complexity: O(?)
        Space Complexity: O(?)
        """

        # dp[i] must represent the length of the longest increasing subsequence 
        # that ends exactly at index i, using nums[i] as the final number in 
        # that sequence.

        size = len(nums)
        # minimum increasing subsequence of length is 1
        dp = [1]*size
        for i in range(0,size):
            for j in reversed(range(0, i)):

                # look backward as is it smaller than me?
                if nums[j] < nums[i]:
                    # Does attaching my number better than already has?
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)                


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.lengthOfLIS([0, 1, 0, 3, 2, 3])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.lengthOfLIS([4,10,4,3,8,9])
    print(f"Test 3: {result}")