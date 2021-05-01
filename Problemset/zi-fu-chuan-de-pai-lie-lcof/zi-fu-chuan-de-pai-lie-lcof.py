
# @Title: 字符串的排列 (字符串的排列  LCOF)
# @Author: 18015528893
# @Date: 2021-02-12 11:47:31
# @Runtime: 200 ms
# @Memory: 19.3 MB

class Solution:
    def permutation(self, s: str) -> List[str]:
        result = []
        s = sorted(s)
        
        def backtrack(path):
            if len(path) == len(s):
                result.append(''.join(path))

            for i in range(len(s)):
                if s[i] is None:
                    continue
                if i > 0 and s[i] == s[i-1]:
                    continue
                path.append(s[i])
                s[i] = None
                backtrack(path)
                s[i] = path.pop()
        
        backtrack([])
        return result
