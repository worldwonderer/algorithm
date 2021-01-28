
# @Title: 整数反转 (Reverse Integer)
# @Author: 18015528893
# @Date: 2019-10-21 21:21:30
# @Runtime: 32 ms
# @Memory: 13.5 MB

class Solution:
    def reverse(self, x: int) -> int:
        s = ''
        sign = True
        if x < 0:
            x = -x
            sign = False
        while True:
            s += str(x % 10)
            x = x // 10
            if x == 0:
                break
        if sign is False:
            s = -int(s)
        else:
            s = int(s)
        if s > 2**31-1 or s < -2**31:
            return 0
        return s
        
