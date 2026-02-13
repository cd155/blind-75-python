"""
LeetCode 139: Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into
a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters
- All the strings of wordDict are unique
"""


class Solution:
    def wordBreak(self, s, wordDict):
        """
        Determine if string can be segmented into dictionary words.

        Args:
            s: Input string
            wordDict: List of valid words

        Returns:
            True if s can be segmented, False otherwise

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.wordBreak("leetcode", ["leet", "code"])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.wordBreak("applepenapple", ["apple", "pen"])
    print(f"Test 2: {result}")
