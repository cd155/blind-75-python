"""
LeetCode 53: Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def maxSubArray(self, nums):
        """
        Find the contiguous subarray with the largest sum.

        Args:
            nums: List of integers

        Returns:
            Maximum subarray sum

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.maxSubArray([1])
    print(f"Test 2: {result}")
