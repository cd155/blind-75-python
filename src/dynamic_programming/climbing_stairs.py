"""
LeetCode 70: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
- 1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n):
        """
        Calculate the number of ways to climb n stairs.

        Args:
            n: Number of stairs

        Returns:
            Number of distinct ways

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        stair_to_num_ways = {0: 1, 1: 1}

        def climb(n_stair):
            if n_stair in stair_to_num_ways:
                return stair_to_num_ways[n_stair]
            else:
                num_of_ways = climb(n_stair-1) + climb(n_stair-2)
                stair_to_num_ways[n_stair] = num_of_ways
                return num_of_ways       

        return climb(n)


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.climbStairs(2)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.climbStairs(3)
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.climbStairs(8)
    print(f"Test 3: {result}")
