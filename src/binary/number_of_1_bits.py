"""
LeetCode 191: Number of 1 Bits

Write a function that takes the binary representation of a positive integer and returns the number of
set bits it has (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation: The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation: The input binary string 10000000 has a total of one set bit.

Constraints:
- 1 <= n <= 2^31 - 1
"""


class Solution:
    def hammingWeight(self, n):
        """
        Count the number of 1 bits in an integer.

        Args:
            n: Positive integer

        Returns:
            Number of 1 bits

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.hammingWeight(11)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.hammingWeight(128)
    print(f"Test 2: {result}")
