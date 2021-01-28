
# @Title: 打印从1到最大的n位数 (打印从1到最大的n位数 LCOF)
# @Author: 18015528893
# @Date: 2021-01-17 18:57:24
# @Runtime: 44 ms
# @Memory: 20.2 MB

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10 ** n))

