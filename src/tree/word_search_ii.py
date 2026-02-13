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


class Solution:
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
        # TODO: Implement solution
        pass


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
