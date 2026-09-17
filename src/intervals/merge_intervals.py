"""
LeetCode 56: Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4
"""


class Solution:
    def merge(self, intervals):
        """
        Merge overlapping intervals.

        Args:
            intervals: List[List[int]] - list of intervals

        Returns:
            List[List[int]] - merged intervals

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        result = []
        intervals.sort(key=lambda x: x[0])
        size = len(intervals)
        temp_start, temp_end = intervals[0][0], intervals[0][1]
        for i in range(1, size):
            if intervals[i][0] <= temp_end:
                temp_end = max(temp_end, intervals[i][1])
            else:
                result.append([temp_start, temp_end])
                temp_start, temp_end = intervals[i][0], intervals[i][1]
        result.append([temp_start, temp_end])

        return result


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.merge([[1, 4], [4, 5]])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.merge([[1,4], [0,0]])
    print(f"Test 3: {result}")