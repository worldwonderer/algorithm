
# @Title: N 皇后 (N-Queens)
# @Author: 18015528893
# @Date: 2021-02-22 20:55:20
# @Runtime: 120 ms
# @Memory: 15.4 MB

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.']*n for _ in range(n)]

        def is_valid(row, col):
            n = len(board)
            for i in range(n):
                if board[i][col] == 'Q':
                    return False

            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == 'Q':
                    return False

            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            return True
        
        def backtrack(i):
            if i == n:
                ans.append(["".join(line) for line in board])
                return 

            for j in range(n):
                if not is_valid(i, j):
                    continue
                board[i][j] = 'Q'
                backtrack(i+1)
                board[i][j] = '.'
            
        backtrack(0)
        return ans

