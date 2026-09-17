"""
LeetCode 371: Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:
- -1000 <= a, b <= 1000
"""


class Solution:
    def getSum(self, a, b):
        """
        Calculate sum of two integers without using + or - operators.

        Args:
            a: First integer
            b: Second integer

        Returns:
            Sum of a and b

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # 32 digits binary with all 1
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        carry_digit, sum_digit = 1, 1
        while carry_digit != 0:
            sum_digit = (a ^ b) & MASK
            carry_digit = ((a & b) << 1) & MASK
            a, b = sum_digit, carry_digit

        if sum_digit > MAX_INT:
            # mathematical trick flip the 32 digital, then flip entire
            return ~(sum_digit ^ MASK)
        return sum_digit


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.getSum(1, 2)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.getSum(-1, 3)
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.getSum(5, 0)
    print(f"Test 3: {result}")