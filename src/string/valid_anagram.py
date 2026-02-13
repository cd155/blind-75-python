"""
LeetCode 242: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s, t):
        """
        Check if two strings are anagrams.

        Args:
            s: str - first string
            t: str - second string

        Returns:
            bool - true if t is anagram of s

        Time Complexity: O(n)
        Space Complexity: O(1) - fixed alphabet size
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.isAnagram("anagram", "nagaram")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.isAnagram("rat", "car")
    print(f"Test 2: {result}")
