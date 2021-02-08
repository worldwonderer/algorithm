
# @Title: 电话号码的字母组合 (Letter Combinations of a Phone Number)
# @Author: 18015528893
# @Date: 2021-02-08 15:45:29
# @Runtime: 32 ms
# @Memory: 15.1 MB

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(track, i):
            if len(track) == len(digits):
                result.append(''.join(track))
                return

            choices = m[digits[i]]
            for choice in choices:
                track.append(choice)
                backtrack(track, i+1)
                track.pop()

        if len(digits) == 0:
            return []
        backtrack([], 0)
        return result

