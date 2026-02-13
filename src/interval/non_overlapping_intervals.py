"""
LeetCode 435: Non-overlapping Intervals

Given an array of intervals where intervals[i] = [starti, endi], return the minimum number of
intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2

Constraints:
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
"""


class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        Find minimum number of intervals to remove to make non-overlapping.

        Args:
            intervals: List[List[int]] - list of intervals

        Returns:
            int - minimum number of intervals to remove

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])
    print(f"Test 2: {result}")
