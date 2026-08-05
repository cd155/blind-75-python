"""
LeetCode 647: Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.
"""


class Solution:
    def countSubstrings(self, s):
        """
        Count the number of palindromic substrings.

        Args:
            s: str - input string

        Returns:
            int - number of palindromic substrings

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        size = len(s)
        result = 0
        
        def count_expand_around_center(left, right):
            count = 0
            while(left >= 0 and right < size and s[left] == s[right]):
                left -=1
                right += 1
                count += 1
            return count

        for i in range(size):
            result += count_expand_around_center(i, i)
            result += count_expand_around_center(i, i+1)
        return result


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.countSubstrings("abc")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.countSubstrings("aaa")
    print(f"Test 2: {result}")
