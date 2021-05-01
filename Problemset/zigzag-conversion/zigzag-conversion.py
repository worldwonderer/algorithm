
# @Title: Z 字形变换 (ZigZag Conversion)
# @Author: 18015528893
# @Date: 2021-02-21 11:51:14
# @Runtime: 64 ms
# @Memory: 15.1 MB

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        ans = ["" for _ in range(numRows)]
        flag = -1
        i = 0
        for char in s:
            ans[i] += char
            if i == 0 or i == numRows-1:
                flag = -flag
            i += flag
        return ''.join(ans)


