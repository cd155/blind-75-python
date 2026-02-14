"""
LeetCode 152: Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any prefix or suffix is guaranteed to fit in a 32-bit integer
"""


class Solution:
    def maxProduct(self, nums):
        """
        Find the contiguous subarray with the largest product.

        Args:
            nums: List of integers

        Returns:
            Maximum product

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        global_max = nums[0]
        max_n, min_n = nums[0], nums[0]
        for num in nums[1:]:
            temp_max_n = max(num, max_n*num, min_n*num)
            min_n = min(num, min_n*num, max_n*num)
            max_n = temp_max_n
            global_max = max(global_max, max_n)
        return global_max


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.maxProduct([2, 3, -2, 4])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.maxProduct([-2, 0, -1])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.maxProduct([-4, -3, -2])
    print(f"Test 3: {result}")
