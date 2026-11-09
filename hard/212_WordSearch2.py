# 212. Word Search II - https://leetcode.com/problems/word-search-ii/description/

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

################################### Solution ###################################

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS = len(board)
        COLS = len(board[0])
        res, path = set(), set()

        def backtracking(r, c, node, word):
            if (
                r < 0
                or c < 0
                or c >= COLS
                or r >= ROWS
                or (r, c) in path
                or board[r][c] not in node.children
            ):
                return

            path.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            backtracking(r + 1, c, node, word)
            backtracking(r - 1, c, node, word)
            backtracking(r, c - 1, node, word)
            backtracking(r, c + 1, node, word)

            path.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                backtracking(r, c, root, "")
        return list(res)
