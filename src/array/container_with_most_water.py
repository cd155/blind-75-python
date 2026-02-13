"""
LeetCode 11: Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that
the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""


class Solution:
    def maxArea(self, height):
        """
        Find the maximum area of water that can be contained.

        Args:
            height: List of heights

        Returns:
            Maximum area

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.maxArea([1, 1])
    print(f"Test 2: {result}")
