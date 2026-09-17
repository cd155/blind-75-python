"""
LeetCode 211: Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches any
previously added string.

Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that matches word
  or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:
Input: ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
       [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output: [null,null,null,null,false,true,true,true]

Constraints:
- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
"""


class WordDictionary:
    def __init__(self):
        """
        Initialize the word dictionary.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement initialization
        pass

    def addWord(self, word):
        """
        Add a word to the dictionary.

        Args:
            word: str - word to add

        Time Complexity: O(m) where m is word length
        Space Complexity: O(m)
        """
        # TODO: Implement addWord
        pass

    def search(self, word):
        """
        Search for a word (may contain wildcards).

        Args:
            word: str - word to search (may contain '.')

        Returns:
            bool - true if word matches

        Time Complexity: O(m) for words without '.', O(m * 26^k) worst case
        Space Complexity: O(m) for recursion
        """
        # TODO: Implement search
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(f"Search 'pad': {wordDictionary.search('pad')}")  # False
    print(f"Search 'bad': {wordDictionary.search('bad')}")  # True
    print(f"Search '.ad': {wordDictionary.search('.ad')}")  # True
    print(f"Search 'b..': {wordDictionary.search('b..')}")  # True
