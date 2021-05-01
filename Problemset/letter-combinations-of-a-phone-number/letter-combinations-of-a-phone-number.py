
# @Title: 电话号码的字母组合 (Letter Combinations of a Phone Number)
# @Author: 18015528893
# @Date: 2021-02-18 10:56:55
# @Runtime: 44 ms
# @Memory: 15 MB

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

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
        ans = []
        def backtrack(path):
            if len(path) == len(digits):
                ans.append(''.join(path))
                return

            choices = m[digits[len(path)]]
            for char in choices:
                path.append(char)
                backtrack(path)
                path.pop()

        backtrack([])
        return ans


