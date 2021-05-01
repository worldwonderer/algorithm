class Solution:
    def strToInt(self, str: str) -> int:
        s = str.strip()
        if s == '':
            return 0
        if s[0] == '+':
            sign = 1
            i = 1
        elif s[0] == '-':
            sign = -1
            i = 1
        else:
            sign = 1
            i = 0
        res = 0
        boundary = (2**31-1) // 10
        while i < len(s):
            c = s[i]
            if not '0' <= c <= '9':
                break
            int_c = ord(c) - ord('0')
            if (res == boundary and int_c > 7) or res > boundary:
                return -2147483648 if sign == -1 else 2147483647
            else:
                res = res * 10 + int_c
            i += 1
        return sign * res
