"""
LeetCode 347: Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array]
"""
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        Find the k most frequent elements.

        Args:
            nums: List[int] - array of integers
            k: int - number of top frequent elements

        Returns:
            List[int] - k most frequent elements

        Time Complexity: O(n log k) with heap, O(n) with bucket sort
        Space Complexity: O(n)
        """
        num_to_count_dict = {}
        for num in nums:
            if num in num_to_count_dict:
                num_to_count_dict[num] += 1
            else:
                num_to_count_dict[num] = 1

        my_heap = []

        for num in num_to_count_dict:
            if len(my_heap) < k:
                heapq.heappush(my_heap, (num_to_count_dict[num], num))
            elif (num_to_count_dict[num] > my_heap[0][0]):
                heapq.heapreplace(my_heap, (num_to_count_dict[num], num))

        return [num for (_,num) in my_heap]

# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.topKFrequent([1], 1)
    print(f"Test 2: {result}")
