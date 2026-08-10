"""
LeetCode 57: Insert Interval

You are given an array of non-overlapping intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order
by starti. You are also given an interval newInterval = [start, end] that represents the start
and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
"""


class Solution:
    def insert(self, intervals, newInterval):
        """
        Insert a new interval into a sorted list of intervals.

        Args:
            intervals: List[List[int]] - sorted non-overlapping intervals
            newInterval: List[int] - interval to insert

        Returns:
            List[List[int]] - merged intervals

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        size = len(intervals)
        result = []
        start_insert, end_insert = newInterval

        i = 0
        while i < size and start_insert > intervals[i][1]:
            result.append(intervals[i])
            i += 1

        while i < size and end_insert >= intervals[i][0]:
            start_insert = min(start_insert, intervals[i][0])
            end_insert = max(end_insert, intervals[i][1])
            i += 1
        result.append(newInterval)

        while i < size:
            result.append(intervals[i])
            i += 1

        return result


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.insert([[1, 3], [6, 9]], [2, 5])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.insert([], [4, 8])
    print(f"Test 3: {result}")

    # Test case 4
    result = solution.insert([[1,5]], [2, 3])
    print(f"Test 4: {result}")
