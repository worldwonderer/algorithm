
# @Title: 求1+2+…+n (求1+2+…+n LCOF)
# @Author: 18015528893
# @Date: 2021-02-02 21:45:56
# @Runtime: 48 ms
# @Memory: 22.8 MB

class Solution:
    res = 0
    
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res

