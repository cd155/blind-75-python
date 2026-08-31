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
        hash_t = {}
        for c in t:
            if c in hash_t:
                hash_t[c] += 1
            else:
                hash_t[c] = 1

        hash_s = {}
        for c in t:
            hash_s[c] = 0

        required, formed = len(hash_t), 0
        min_length, result = float('inf'), ''
        left = 0

        for i in range(len(s)):
            if s[i] in hash_s:
                hash_s[s[i]] += 1

            if s[i] in hash_s and hash_s[s[i]] == hash_t[s[i]]:
                formed += 1

            if formed == required:
                for j in range(left, i+1):
                    if (i-left+1) < min_length:
                        min_length, result = i-left+1, s[left: i+1]

                    if s[j] in hash_s:
                        if hash_s[s[j]] > hash_t[s[j]]:
                            hash_s[s[j]] -= 1
                            left += 1
                        else:
                            break
                    else:
                        left += 1

        return result


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.minWindow("ADOBECODEBANC", "ABC")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.minWindow("a", "a")
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.minWindow("a", "aa")
    print(f"Test 3: {result}")
