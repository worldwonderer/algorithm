
# @Title: 二进制求和 (Add Binary)
# @Author: 18015528893
# @Date: 2021-02-23 22:45:26
# @Runtime: 44 ms
# @Memory: 15.2 MB

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry == 1:
            v1 = int(a[i]) if i >= 0 else 0
            v2 = int(b[j]) if j >= 0 else 0

            total = v1 + v2 + carry
            if total >= 2:
                total -= 2
                carry = 1
            else:
                carry = 0
            print(total)
            ans = str(total) + ans
            i -= 1
            j -= 1
        return ans

