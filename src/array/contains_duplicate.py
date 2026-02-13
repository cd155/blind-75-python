"""
LeetCode 217: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        Check if array contains any duplicates.

        Args:
            nums: List of integers

        Returns:
            True if duplicates exist, False otherwise

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        num_to_int = {}
        for num in nums:
            if num in num_to_int:
                return True
            else:
                num_to_int[num] = 1
        return False


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.containsDuplicate([1, 2, 3, 1])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.containsDuplicate([1, 2, 3, 4])
    print(f"Test 2: {result}")
