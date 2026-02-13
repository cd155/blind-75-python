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
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.minMeetingRooms([[7, 10], [2, 4]])
    print(f"Test 2: {result}")
