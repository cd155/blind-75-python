"""
LeetCode 424: Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change
it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing
the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s, k):
        """
        Find longest substring with same letter after k replacements.

        Args:
            s: str - input string
            k: int - max number of replacements

        Returns:
            int - length of longest substring

        Time Complexity: O(n)
        Space Complexity: O(1) - fixed size alphabet
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.characterReplacement("ABAB", 2)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.characterReplacement("AABABBA", 1)
    print(f"Test 2: {result}")
