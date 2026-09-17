"""
LeetCode 49: Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        Group strings that are anagrams of each other.

        Args:
            strs: List[str] - array of strings

        Returns:
            List[List[str]] - grouped anagrams

        Time Complexity: O(n * k log k) where k is max string length
        Space Complexity: O(n * k)
        """
        start_index = ord('a')
        tuple_to_anagrams = {}

        for my_str in strs:
            alphabet_to_num = [0] * 26

            for c in my_str:
                i = ord(c) - start_index
                alphabet_to_num[i] += 1

            arry_to_tuple = tuple(alphabet_to_num)
            if arry_to_tuple in tuple_to_anagrams:
                tuple_to_anagrams[arry_to_tuple].append(my_str)
            else:
                tuple_to_anagrams[arry_to_tuple] = [my_str]

        return list(tuple_to_anagrams.values())


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.groupAnagrams([""])
    print(f"Test 2: {result}")
