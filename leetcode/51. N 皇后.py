from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(board, row):
            if row == len(board):
                res.append([''.join(line) for line in board])
                return

            i = len(board[row])
            for col in range(i):
                if not is_valid(board, row, col):
                    continue

                board[row][col] = 'Q'
                backtrack(board, row+1)
                board[row][col] = '.'

        def is_valid(board, row, col):
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

        board = [['.'] * n for _ in range(n)]
        backtrack(board, 0)
        return res

if __name__ == '__main__':
    s = Solution()
    s.solveNQueens(4)


