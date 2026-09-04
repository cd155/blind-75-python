"""
LeetCode 125: Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: s = "race a car"
Output: false

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""


from collections import deque
class Solution:
    def isPalindrome(self, s):
        """
        Check if a string is a valid palindrome.

        Args:
            s: str - input string

        Returns:
            bool - true if palindrome

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        s_clean = [c.lower() for c in s]
        s_clean = [c for c in s_clean if c.isalnum()]
        size = len(s_clean)

        if size%2 == 1:
            return s_clean[0: size//2] == s_clean[size//2+1: size][::-1]
        else:
            return s_clean[0: size//2] == s_clean[size//2: size][::-1]

    def is_palindrome_stack(self, s):
        pass

    def is_palindrome_pointers(self, s):
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.isPalindrome("A man, a plan, a canal: Panama")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.isPalindrome("race a car")
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.isPalindrome("0P")
    print(f"Test 3: {result}")
