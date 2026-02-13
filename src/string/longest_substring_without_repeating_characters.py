"""
LeetCode 3: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Find length of longest substring without repeating characters.

        Args:
            s: str - input string

        Returns:
            int - length of longest substring

        Time Complexity: O(n)
        Space Complexity: O(min(n, m)) where m is charset size
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.lengthOfLongestSubstring("abcabcbb")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.lengthOfLongestSubstring("bbbbb")
    print(f"Test 2: {result}")
