"""
LeetCode 253: Meeting Rooms II

Given an array of meeting time intervals where intervals[i] = [starti, endi], return the minimum
number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
- 1 <= intervals.length <= 10^4
- 0 <= starti < endi <= 10^6
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        """
        Find minimum number of conference rooms required.

        Args:
            intervals: List[List[int]] - meeting time intervals

        Returns:
            int - minimum number of rooms

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        intervals.sort(key=lambda x:x[0])
        size = len(intervals)
        h = [intervals[0][1]]

        for s, e in intervals[1:size]:
            if s >= h[0]:
                heapq.heapreplace(h, e)
            else:
                heapq.heappush(h, e)
                
        return len(h)


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.minMeetingRooms([[7, 10], [2, 4]])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.minMeetingRooms([[1,5],[2,6],[3,7],[4,8],[5,9]])
    print(f"Test 3: {result}")
