"""
LeetCode 20: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s):
        """
        Check if parentheses string is valid.

        Args:
            s: str - string of parentheses

        Returns:
            bool - true if valid

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.isValid("()")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.isValid("()[]{}")
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.isValid("(]")
    print(f"Test 3: {result}")
