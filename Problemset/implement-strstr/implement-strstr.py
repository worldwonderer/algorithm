
# @Title: 实现 strStr() (Implement strStr())
# @Author: 18015528893
# @Date: 2019-10-22 00:26:05
# @Runtime: 44 ms
# @Memory: 13.7 MB

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if len(haystack) < len(needle):
            return -1
        h_p, n_p = 0, 0
        while True:
            if needle[n_p] == haystack[h_p]:
                n_p += 1
                h_p += 1
                if n_p >= len(needle):
                    return h_p-len(needle)
            else:
                h_p = h_p + 1 - n_p
                n_p = 0
            if h_p >= len(haystack):
                return -1
