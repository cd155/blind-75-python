"""
LeetCode 252: Meeting Rooms

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a
person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
"""


class Solution:
    def canAttendMeetings(self, intervals):
        """
        Determine if a person can attend all meetings.

        Args:
            intervals: List[List[int]] - meeting time intervals

        Returns:
            bool - true if can attend all meetings

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.canAttendMeetings([[0, 30], [5, 10], [15, 20]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.canAttendMeetings([[7, 10], [2, 4]])
    print(f"Test 2: {result}")
