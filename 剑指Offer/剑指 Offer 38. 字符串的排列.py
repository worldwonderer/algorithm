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
