
# @Title: 有效的数独 (Valid Sudoku)
# @Author: 18015528893
# @Date: 2021-02-21 23:30:24
# @Runtime: 56 ms
# @Memory: 14.9 MB

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        block = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                pos = i // 3 * 3 + j // 3
                if val in row[i] or val in col[j] or val in block[pos]:
                    return False
                else:
                    row[i].add(val)
                    col[j].add(val)
                    block[pos].add(val)
        return True

