"""
LeetCode 269: Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order among letters
is unknown to you. You are given a list of strings words from the alien language's dictionary,
where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically
increasing order by the new language's rules. If there is no solution, return "". If there are
multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of only lowercase English letters.
"""


class Solution:
    def alienOrder(self, words):
        """
        Determine the order of letters in an alien dictionary.

        Args:
            words: List[str] - sorted words in alien language

        Returns:
            str - order of letters in alien language

        Time Complexity: O(C) where C is total length of all words
        Space Complexity: O(1) since at most 26 letters
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.alienOrder(["z", "x"])
    print(f"Test 2: {result}")
