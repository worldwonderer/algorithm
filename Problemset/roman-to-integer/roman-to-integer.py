
# @Title: 罗马数字转整数 (Roman to Integer)
# @Author: 18015528893
# @Date: 2021-02-19 10:44:33
# @Runtime: 56 ms
# @Memory: 14.8 MB

class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0

        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = 0
        pre_num = m[s[0]]
        for cur in range(1, len(s)):
            cur_num = m[s[cur]]
            if pre_num < cur_num:
                ans -= pre_num
            else:
                ans += pre_num
            pre_num = cur_num
        ans += pre_num
        return ans

