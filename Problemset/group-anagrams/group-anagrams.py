
# @Title: 字母异位词分组 (Group Anagrams)
# @Author: 18015528893
# @Date: 2021-02-20 11:34:50
# @Runtime: 68 ms
# @Memory: 19.8 MB

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            m = [0] * 26
            for char in s:
                idx = ord(char) - ord('a')
                m[idx] += 1
            ans[tuple(m)].append(s)

        return list(ans.values())




