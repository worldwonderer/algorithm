
# @Title: 单词搜索 (Word Search)
# @Author: 18015528893
# @Date: 2021-02-28 12:32:02
# @Runtime: 204 ms
# @Memory: 17.1 MB

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtrack(path, visited, i, j):
            if len(path) == len(word):
                return True
            
            choices = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

            for choice in choices:
                x, y = choice
                if (x, y) in visited or x < 0 or y < 0 or x >= m or y >= n or word[len(path)] != board[x][y]:
                    continue
                visited.add((x, y))
                path.append(board[x][y])
                if backtrack(path, visited, x, y):
                    return True
                path.pop()
                visited.remove((x, y))


        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    if backtrack([word[0]], {(row, col)}, row, col):
                        return True
        return False
