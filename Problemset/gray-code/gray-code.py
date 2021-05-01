
# @Title: 格雷编码 (Gray Code)
# @Author: 18015528893
# @Date: 2021-03-03 10:25:50
# @Runtime: 168 ms
# @Memory: 18.1 MB

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []

        def backtrack(path, choices=('0', '1')):
            if len(path) == n:
                num = int(''.join(path), 2)
                ans.append(num)
                return

            path.append(choices[0])
            backtrack(path, ('0', '1'))
            path.pop()

            path.append(choices[1])
            backtrack(path, ('1', '0'))
            path.pop()

        backtrack([])
        return ans

