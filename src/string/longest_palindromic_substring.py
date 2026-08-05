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
        size = len(s)

        def expand_around_center(left, right):
            while (left >= 0 and right < size and s[left] == s[right]):
                left -= 1
                right += 1
            return left+1, right-1

        result  = 0, 0
        for i in range(0, size):
            # examine palindrome in odd case
            left, right = expand_around_center(i-1, i+1)
            if(right-left) > (result[1] - result[0]):
                result = left, right

            # examine palindrome in even case
            left, right = expand_around_center(i, i+1)
            if(right-left) > (result[1] - result[0]):
                result = left, right

        return s[result[0]:(result[1]+1)]

# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.longestPalindrome("babad")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.longestPalindrome("cbbd")
    print(f"Test 2: {result}")
