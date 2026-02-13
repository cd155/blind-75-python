"""
LeetCode 1: Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists
"""


class Solution:
    def twoSum(self, nums, target):
        """
        Find two numbers that add up to target.

        Args:
            nums: List of integers
            target: Target sum

        Returns:
            List of two indices

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.twoSum([3, 2, 4], 6)
    print(f"Test 2: {result}")
