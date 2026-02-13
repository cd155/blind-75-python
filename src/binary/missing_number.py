"""
LeetCode 268: Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number
in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2

Example 2:
Input: nums = [0,1]
Output: 2

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique
"""


class Solution:
    def missingNumber(self, nums):
        """
        Find the missing number in a range [0, n].

        Args:
            nums: List of distinct numbers

        Returns:
            The missing number

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.missingNumber([3, 0, 1])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.missingNumber([0, 1])
    print(f"Test 2: {result}")
