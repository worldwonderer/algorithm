
# @Title: 二进制求和 (Add Binary)
# @Author: 18015528893
# @Date: 2019-10-22 23:33:10
# @Runtime: 64 ms
# @Memory: 13.6 MB

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = -1
        r = 0
        ret = ''
        while True:
            m = None
            n = None
            try:
                m = int(a[i])
            except IndexError:
                pass
            try:
                n = int(b[i])
            except IndexError:
                pass
            if m is None and n is None:
                break
            if m is None:
                m = 0
            if n is None:
                n = 0
            if m + n + r == 2:
                ret = '0' + ret
                r = 1
            elif m + n + r == 3:
                ret = '1' + ret
                r = 1
            elif m + n + r == 1:
                ret = '1' + ret
                r = 0
            elif m + n + r == 0:
                ret = '0' + ret
                r = 0
            i -= 1
        if r == 1:
            ret = '1' + ret
        return ret
                
