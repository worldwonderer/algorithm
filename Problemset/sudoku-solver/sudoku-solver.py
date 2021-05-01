
# @Title: 解数独 (Sudoku Solver)
# @Author: 18015528893
# @Date: 2021-02-21 23:45:22
# @Runtime: 528 ms
# @Memory: 15.1 MB

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(i, j, val):
            for n in range(9):
                if board[n][j] == val:
                    return False
                if board[i][n] == val:
                    return False
                if board[i//3*3 + n//3][j//3*3+n%3] == val:
                    return False
            return True


        def backtrack(i, j):
            if j == 9:
                return backtrack(i+1, 0)
            if i == 9:
                return True
            if board[i][j] != '.':
                return backtrack(i, j+1)

            for val in range(1, 10):
                val = str(val)
                if not valid(i, j, val):
                    continue
                board[i][j] = val
                if backtrack(i, j+1):
                    return True
                board[i][j] = '.'
        
        backtrack(0, 0)

