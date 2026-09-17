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
        max_word_length = max(len(word) for word in wordDict)
        size = len(s)
        result = [False]*size
        word_dict_set = set(wordDict)

        for end in range(1, size+1):
            for w_length in range(1, max_word_length+1):
                start = end - w_length
                if start>=0 and s[start:end] in word_dict_set:
                    # base case
                    if start-1 < 0:
                        result[end-1] = True
                    else:
                        result[end-1] = result[start-1] or result[end-1]
        return result[-1]

    def word_break_def(self, s, wordDict):
        max_word_length = max(len(word) for word in wordDict)
        size = len(s)

        word_dict_set = set(wordDict)

        def dfs (start):
            if start == size:
                return True

            if start > size:
                return False
            
            for i in range(max_word_length+1):
                end = start+i
                if s[start: end] in word_dict_set:
                    if (dfs(end)):
                        return True
            return False

        return dfs(0)


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.wordBreak("dogs", ["dog", "s", "gs"])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.wordBreak("applepenapple", ["apple", "pen"])
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.wordBreak("catsincars", ["cats","cat","sin","in","car"])
    print(f"Test 3: {result}")
