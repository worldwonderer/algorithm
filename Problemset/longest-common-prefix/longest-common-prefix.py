
# @Title: 最长公共前缀 (Longest Common Prefix)
# @Author: 18015528893
# @Date: 2019-10-21 22:04:20
# @Runtime: 36 ms
# @Memory: 13.5 MB

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        result = ''
        i = 0
        while True:
            f = None
            for s in strs:
                try:
                    if f is None:
                        f = s[i]
                    else:
                        if f != s[i]:
                            return result
                except IndexError:
                    return result
            if f is not None:
                result += f
            i += 1
        return result
            
