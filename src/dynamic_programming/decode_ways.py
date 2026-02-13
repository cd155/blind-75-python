"""
LeetCode 91: Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the
reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Given a string s containing only digits, return the number of ways to decode it.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3

Constraints:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s)
"""


class Solution:
    def numDecodings(self, s):
        """
        Count the number of ways to decode the string.

        Args:
            s: Encoded string of digits

        Returns:
            Number of ways to decode

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.numDecodings("12")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.numDecodings("226")
    print(f"Test 2: {result}")
