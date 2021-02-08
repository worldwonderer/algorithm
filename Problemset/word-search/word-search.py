
# @Title: 单词搜索 (Word Search)
# @Author: 18015528893
# @Date: 2021-02-08 23:37:27
# @Runtime: 252 ms
# @Memory: 16.8 MB

from typing import List

class Solution:
    def __init__(self):
        self.board = None
        self.word = None

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.backtrace([board[row][col]], {(row, col)}, row, col):
                        return True
        return False

    def backtrace(self, path, visited, i, j):
        if len(path) == len(self.word):
            return True

        around_ij = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for x, y in around_ij:
            if x < 0 or y < 0 or x >= len(self.board) or y >= len(self.board[0]) or (x, y) in visited or self.board[x][y] != self.word[len(visited)]:
                continue
            path.append(self.board[x][y])
            visited.add((x, y))
            if self.backtrace(path, visited, x, y):
                return True
            path.pop()
            visited.remove((x, y))



