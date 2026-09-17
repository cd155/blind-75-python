"""
LeetCode 1143: Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining characters.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters
"""


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        """
        Find the length of the longest common subsequence.

        Args:
            text1: First string
            text2: Second string

        Returns:
            Length of longest common subsequence

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.longestCommonSubsequence("abcde", "ace")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.longestCommonSubsequence("abc", "abc")
    print(f"Test 2: {result}")
