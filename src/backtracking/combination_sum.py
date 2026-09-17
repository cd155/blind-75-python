"""
LeetCode 39: Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all
unique combinations of candidates where the chosen numbers sum to target. You may return the combinations
in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique
if the frequency of at least one of the chosen numbers is different.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Constraints:
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct
- 1 <= target <= 40
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        Find all unique combinations that sum to target.

        Args:
            candidates: List of distinct integers
            target: Target sum

        Returns:
            List of combinations

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.combinationSum([2, 3, 6, 7], 7)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.combinationSum([2, 3, 5], 8)
    print(f"Test 2: {result}")
