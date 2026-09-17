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

    def three_sum_hash(self, nums):
        size = len(nums)
        sorted_nums = sorted(nums)
        result = []
        for i in range(size):
            if i>0 and sorted_nums[i]==sorted_nums[i-1]:
                continue
            records = set()
            j = i+1
            while j<size:
                complement = -(sorted_nums[i] + sorted_nums[j]) 
                if complement in records:
                    new_list = [sorted_nums[i], sorted_nums[j], complement]
                    result.append(new_list)
                    while j+1<size and sorted_nums[j] == sorted_nums[j+1]:
                        j+=1
                records.add(sorted_nums[j])
                j+=1
        return result

    def three_sum_two_pointers(self, nums):
        size = len(nums)
        sorted_nums = sorted(nums)
        result = []

        for i in range(size):
            if i>0 and sorted_nums[i]==sorted_nums[i-1]:
                continue
            left, right = i+1, size-1
            while left < right:
                sum_two = sorted_nums[left] + sorted_nums[right]
                if sum_two < -sorted_nums[i]:
                    left += 1
                elif sum_two > -sorted_nums[i]:
                    right -= 1
                else:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    while left+1 < size and sorted_nums[left] == sorted_nums[left+1]:
                        left += 1

                    while right-1 > 0 and sorted_nums[right] == sorted_nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
        return result

# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.three_sum_two_pointers([-1, 0, 1, 2, -1, -4])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.three_sum_two_pointers([0, 1, 1])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.three_sum_two_pointers([2, -1, -4])
    print(f"Test 3: {result}")

    # Test case 4
    result = solution.three_sum_two_pointers([0, 0, 0])
    print(f"Test 4: {result}")

    # Test case 5
    result = solution.three_sum_two_pointers([0, 0, 1, 0])
    print(f"Test 5: {result}")

    # Test case 6
    result = solution.three_sum_two_pointers([-1, 0, 1])
    print(f"Test 6: {result}")

    # Test case 7
    result = solution.three_sum_two_pointers([0,0,0,0,0,1,1,2])
    print(f"Test 7: {result}")