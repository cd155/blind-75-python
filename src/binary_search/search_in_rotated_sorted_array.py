"""
LeetCode 33: Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index.
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is an ascending array that is possibly rotated
- -10^4 <= target <= 10^4
"""


class Solution:
    def search(self, nums, target):
        """
        Search for a target value in a rotated sorted array.

        Args:
            nums: Rotated sorted array
            target: Target value to search for

        Returns:
            Index of target, or -1 if not found

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.search([4, 5, 6, 7, 0, 1, 2], 0)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.search([4, 5, 6, 7, 0, 1, 2], 3)
    print(f"Test 2: {result}")
