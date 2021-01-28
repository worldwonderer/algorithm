
# @Title: 罗马数字转整数 (Roman to Integer)
# @Author: 18015528893
# @Date: 2019-10-21 21:57:13
# @Runtime: 68 ms
# @Memory: 13.7 MB

class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        if len(s) == 1:
            return value_map[s]
        i = 0
        j = 1
        ret = 0
        while True:
            if value_map[s[j]] > value_map[s[i]]:
                ret += value_map[s[i] + s[j]]
                i += 2
                j += 2
            else:
                ret += value_map[s[i]]
                i += 1
                j += 1
            if i >= len(s):
                break
            if j >= len(s):
                ret += value_map[s[i]]
                break
        return ret

