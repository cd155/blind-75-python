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
        # slow version N^3
        first_p, second_p, third_p = 0, 1, 2
        size = len(nums)
        result = []

        while third_p < size:
            third_p_local = third_p
            for i in range(second_p, size):
                goal = nums[first_p] + nums[i]
                for j in range(third_p_local, size):
                    if nums[j] + goal == 0:
                        new_list = sorted([nums[first_p], nums[i], nums[j]])
                        if new_list not in result:
                            result.append(new_list)
                third_p_local += 1
            first_p += 1 
            second_p += 1
            third_p += 1
        return result

    def three_sum_fast(self, nums):
        p = 1
        size = len(nums)
        sorted_nums = sorted(nums)
        result = []
        for i in range(size):
            records = set()
            for j in range(p, size):
                complement = -(sorted_nums[i] + sorted_nums[j]) 
                if complement in records:
                    new_list = sorted([sorted_nums[i], sorted_nums[j], complement])
                    if new_list not in result:
                        result.append(new_list)
                else:
                    records.add(sorted_nums[j])
            p += 1
        return result


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.three_sum_fast([-1, 0, 1, 2, -1, -4])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.three_sum_fast([0, 1, 1])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.three_sum_fast([2, -1, -4])
    print(f"Test 3: {result}")
