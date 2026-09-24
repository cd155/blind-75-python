"""
LeetCode 79: Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Constraints:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
"""


class Solution:
    def exist(self, board, word):
        """
        Search for a word in a 2D board.

        Args:
            board: List[List[str]] - 2D grid of characters
            word: str - word to search for

        Returns:
            bool - true if word exists in board

        Time Complexity: O(m * n * 4^L) where L is word length
        Space Complexity: O(L) for recursion stack
        """
        m = len(board)
        n = len(board[0])
        max_index = len(word)-1

        def dfs(i,j,word_index):
            if board[i][j] == word[word_index] and board[i][j] != '#':
                if word_index == max_index:
                    return True
                cha = board[i][j]
                board[i][j] = '#'
                word_index += 1
                for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                    next_i, next_j = i + di, j + dj
                    if 0 <= next_i < m and 0 <= next_j < n and word_index <= max_index:
                        if dfs(next_i, next_j, word_index):
                            return True
                board[i][j] = cha

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.exist([["A", "B"], ["C", "D"]], "AD")
    print(f"Test 3: {result}")