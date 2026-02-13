"""
LeetCode 15: 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = [0,1,1]
Output: []

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""


class Solution:
    def threeSum(self, nums):
        """
        Find all unique triplets that sum to zero.

        Args:
            nums: List of integers

        Returns:
            List of triplets that sum to zero

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.threeSum([0, 1, 1])
    print(f"Test 2: {result}")
