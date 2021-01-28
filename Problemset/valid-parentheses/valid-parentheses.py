
# @Title: 有效的括号 (Valid Parentheses)
# @Author: 18015528893
# @Date: 2019-10-21 22:16:38
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            '(':')', 
            '{':'}', 
            '[':']',
        }
        l = list()
        if s == '':
            return True
        if len(s) % 2 == 1:
            return False
        i = 0
        while True:
            if s[i] in m:
                l.append(m[s[i]])
            else:
                if len(l) == 0 or s[i] != l.pop():
                    return False
            i += 1
            if i >= len(s):
                break
        if len(l) != 0:
            return False
        return True
