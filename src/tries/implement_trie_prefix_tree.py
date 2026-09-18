"""
LeetCode 208: Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store
and retrieve keys in a dataset of strings. There are various applications of this data structure,
such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie, and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word
  that has the prefix prefix, and false otherwise.

Example 1:
Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
       [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output: [null, null, true, false, true, null, true]

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        """
        Initialize the trie data structure.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the trie.

        Args:
            word: str - word to insert

        Time Complexity: O(m) where m is word length
        Space Complexity: O(m)
        """
        end_index = len(word)-1
        cur = self.root
        for i, c in enumerate(word):
            new_tri = TrieNode()
            if c not in cur.children:
                cur.children[c] = new_tri
                cur = new_tri
            else:
                cur = cur.children[c]

            if i == end_index:
                cur.is_end = True

    def search(self, word):
        """
        Search for a word in the trie.

        Args:
            word: str - word to search for

        Returns:
            bool - true if word exists

        Time Complexity: O(m)
        Space Complexity: O(1)
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return cur.is_end

    def startsWith(self, prefix):
        """
        Check if any word starts with the given prefix.

        Args:
            prefix: str - prefix to check

        Returns:
            bool - true if prefix exists

        Time Complexity: O(m)
        Space Complexity: O(1)
        """
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return True

    def pretty_print(self, root, word):
        if root.is_end:
            print(word)

        for k, v in root.children.items():
            word.append(k)
            self.pretty_print(v, word)


# Example usage (for testing locally)
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(f"Search 'apple': {trie.search('apple')}")  # True
    print(f"Search 'app': {trie.search('app')}")  # False
    print(f"StartsWith 'app': {trie.startsWith('app')}")  # True
    trie.insert("app")
    print(f"Search 'app': {trie.search('app')}")  # True

    trie = Trie()
    trie.insert("a")
    print(f"Search 'a': {trie.search('a')}")  # True
    print(f"Search 'a': {trie.startsWith('a')}")  # True
