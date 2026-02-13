"""
LeetCode 338: Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]

Constraints:
- 0 <= n <= 10^5
"""


class Solution:
    def countBits(self, n):
        """
        Count the number of 1 bits for each number from 0 to n.

        Args:
            n: Non-negative integer

        Returns:
            Array of bit counts

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.countBits(2)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.countBits(5)
    print(f"Test 2: {result}")
