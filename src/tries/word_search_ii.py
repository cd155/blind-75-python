"""
LeetCode 212: Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once
in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
"""
from implement_trie_prefix_tree import Trie


class Solution:
    def __init__(self):
        self.trie = Trie() 

    def findWords(self, board, words):
        """
        Find all words from the list that exist in the board.

        Args:
            board: List[List[str]] - 2D character board
            words: List[str] - list of words to search for

        Returns:
            List[str] - words found in board

        Time Complexity: O(m * n * 4^L) where L is max word length
        Space Complexity: O(k) where k is total characters in words
        """
        all_possible_words = self.find_all_words(board)
        for p_word in all_possible_words:
            self.trie.insert(p_word)

        result = []
        for f_w in words:
            if self.trie.startsWith(f_w):
                result.append(f_w)
        return result

    def find_all_words(self, board):
        all_paths = []
        m = len(board)
        n = len(board[0])

        def dfs(i, j, visited, path):
            can_move = False
            path.append(board[i][j])
            visited.add((i,j))

            ds = [(1,0), (0,1), (-1,0), (0,-1)]

            for d_i, d_j in ds:
                next_i, next_j = i+d_i, j+d_j
                if 0<=next_i<m and 0<=next_j<n and (next_i,next_j) not in visited:
                    can_move = True
                    dfs(next_i, next_j, visited, path)

            if not can_move:
                all_paths.append(list(path))

            path.pop()
            visited.remove((i,j))
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, set(), [])

        return all_paths


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    result = solution.findWords(board, words)
    print(f"Test 1: {result}")

    # Test case 2
    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    result = solution.findWords(board, words)
    print(f"Test 2: {result}")
