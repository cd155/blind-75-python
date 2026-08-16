"""
LeetCode 190: Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Example 1:
Input: n = 00000010100101000001111010011100
Output: 964176192 (00111001011110000010100101000000)

Example 2:
Input: n = 11111111111111111111111111111101
Output: 3221225471 (10111111111111111111111111111111)

Constraints:
- The input must be a binary string of length 32
"""


class Solution:
    def reverseBits(self, n):
        """
        Reverse the bits of a 32-bit unsigned integer.

        Args:
            n: 32-bit unsigned integer

        Returns:
            Reversed bits as integer

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        result = 0
        for i in range(len(bin(n)) - 2):
            result = (result << 1) | ((n >> i) & 1)
        return result


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.reverseBits(0b00000010100101000001111010011100)
    print(f"Test 1: {bin(result)}")

    # Test case 2
    result = solution.reverseBits(0b11111111111111111111111111111101)
    print(f"Test 2: {bin(result)}")

    # Test case 3
    result = solution.reverseBits(0b11001)
    print(f"Test 3: {bin(result)}")