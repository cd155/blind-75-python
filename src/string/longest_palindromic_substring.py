"""
LeetCode 5: Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s):
        """
        Find the longest palindromic substring.

        Args:
            s: str - input string

        Returns:
            str - longest palindromic substring

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.longestPalindrome("babad")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.longestPalindrome("cbbd")
    print(f"Test 2: {result}")
