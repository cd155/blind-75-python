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
        s_clean = [c.lower() for c in s]
        s_clean = [c for c in s_clean if c.isalnum()]
        size = len(s_clean)

        first_half = s_clean[0: size//2]
        second_half = s_clean[size//2: size]
        if size%2 == 1:
            second_half = s_clean[size//2+1: size]

        for c in second_half:
            if c == first_half[-1]:
                first_half.pop()
            else:
                return False

        if len(first_half) == 0:
            return True
        else:
            return False

    def is_palindrome_pointers(self, s):
        left_p, right_p = 0, len(s)-1

        while left_p < right_p :

            if not s[left_p].isalnum():
                left_p += 1
                continue

            if not s[right_p].isalnum():
                right_p -= 1
                continue

            if s[left_p].lower() != s[right_p].lower():
                return False
            left_p += 1
            right_p -= 1

        return True 


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.is_palindrome_pointers("A man, a plan, a canal: Panama")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.isPalindrome("race a car")
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.isPalindrome("0P")
    print(f"Test 3: {result}")
