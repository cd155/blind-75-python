"""
LeetCode 153: Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique
- nums is sorted and rotated between 1 and n times
"""


class Solution:
    def findMin(self, nums):
        """
        Find the minimum element in a rotated sorted array.

        Args:
            nums: Rotated sorted array

        Returns:
            Minimum element

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.findMin([3, 4, 5, 1, 2])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.findMin([4, 5, 6, 7, 0, 1, 2])
    print(f"Test 2: {result}")
