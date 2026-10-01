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
        dp = []
        m, n = len(text1), len(text2)
        for _ in range(m):
            dp.append([0] * n)
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    prev = 0
                    if i-1 >= 0 and j-1 >= 0:
                        prev = dp[i-1][j-1]
                    dp[i][j] = 1 + prev
                else:
                    max_lcs_1, max_lcs_2 = 0, 0 
                    if i-1 >= 0:
                        max_lcs_1 = dp[i-1][j]
                    if j-1 >= 0:
                        max_lcs_2 = dp[i][j-1]
                    dp[i][j] = max(max_lcs_1, max_lcs_2)
        return dp[m-1][n-1]


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.longestCommonSubsequence("abcde", "ace")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.longestCommonSubsequence("abc", "abc")
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.longestCommonSubsequence("cba", "ab")
    print(f"Test 3: {result}")