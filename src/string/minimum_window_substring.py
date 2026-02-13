"""
LeetCode 76: Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window. If there
is no such substring, return the empty string "".

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.
"""


class Solution:
    def minWindow(self, s, t):
        """
        Find minimum window substring containing all characters of t.

        Args:
            s: str - source string
            t: str - target string

        Returns:
            str - minimum window substring

        Time Complexity: O(m + n)
        Space Complexity: O(m + n)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.minWindow("ADOBECODEBANC", "ABC")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.minWindow("a", "a")
    print(f"Test 2: {result}")
