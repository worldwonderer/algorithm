
# @Title: 字符串相乘 (Multiply Strings)
# @Author: 18015528893
# @Date: 2021-02-22 13:51:22
# @Runtime: 144 ms
# @Memory: 15.1 MB

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        ans = [0] * (m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                s = mul + ans[p2]
                ans[p1] += s // 10
                ans[p2] = s % 10

        i = 0
        while i < len(ans):
            if ans[i] != 0:
                break
            i += 1

        return ''.join([str(x) for x in ans[i:]])


