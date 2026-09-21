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


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        """
        Initialize the word dictionary.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Add a word to the dictionary.

        Args:
            word: str - word to add

        Time Complexity: O(m) where m is word length
        Space Complexity: O(m)
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()            
            cur = cur.children[c]
        cur.is_end = True

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
        max_len = len(word)

        def dfs(node, i):
            if i < max_len:
                if word[i] == '.':
                    for _, v in node.children.items():
                        if dfs(v, i+1):
                            return True
                    return False
                elif word[i] in node.children:
                    return dfs(node.children[word[i]], i+1)
                else:
                    return False
            return node.is_end

        return dfs(self.root, 0)

# Example usage (for testing locally)
if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    wordDictionary.addWord("a")
    wordDictionary.addWord("c")
    wordDictionary.addWord("cat")
    print(f"Search 'pad': {wordDictionary.search('pad')}")  # False
    print(f"Search 'bad': {wordDictionary.search('bad')}")  # True
    print(f"Search '.ad': {wordDictionary.search('.ad')}")  # True
    print(f"Search 'b..': {wordDictionary.search('b..')}")  # True
    print(f"Search '.b': {wordDictionary.search('a.')}")  # False
    print(f"Search '.b': {wordDictionary.search('c.z')}")  # False
