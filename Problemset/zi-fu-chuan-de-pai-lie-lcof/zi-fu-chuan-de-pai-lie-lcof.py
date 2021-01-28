
# @Title: 字符串的排列 (字符串的排列  LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 23:57:50
# @Runtime: 1076 ms
# @Memory: 24.5 MB

from collections import Counter


class Solution:
    def permutation(self, s: str) -> List[str]:
        res = set()
        c = dict(Counter(s))

        def backtrack(s, track):
            if len(s) == len(track):
                res.add(track)
                return

            for char in s:
                if c[char] == 0:
                    continue

                track += char
                c[char] -= 1
                backtrack(s, track)
                track = track[:-1]
                c[char] += 1

        backtrack(s, "")
        return list(res)


