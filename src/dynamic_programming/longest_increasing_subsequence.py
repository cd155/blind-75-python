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
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.lengthOfLIS([0, 1, 0, 3, 2, 3])
    print(f"Test 2: {result}")
