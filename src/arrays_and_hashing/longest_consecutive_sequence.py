"""
LeetCode 128: Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def longestConsecutive(self, nums):
        """
        Find the length of the longest consecutive sequence.

        Args:
            nums: List[int] - array of integers

        Returns:
            int - length of longest consecutive sequence

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        starts = []
        nums_set = set(nums)
        
        for num in nums_set:
            if((num-1) not in nums_set):
                starts.append(num)

        max_length = 0
        for start in starts:
            temp_length = 1
            while(start+1 in nums_set):
                start += 1
                temp_length += 1
            max_length = max(max_length, temp_length)

        return max_length

    def longest_consecutive_dfs(self, nums):

        nums_set = set(nums)
        visited = set()
        max_length = 0

        def dfs(n):
            visited.add(n)
            if n not in nums_set:
                return 0
            else:
                return 1 + dfs(n+1) # set is sorted

        for num in nums_set:
            if num not in visited:
                max_length = max(max_length, dfs(num))

        return max_length

# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.longestConsecutive([100, 4, 200, 1, 3, 2])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    print(f"Test 2: {result}")
