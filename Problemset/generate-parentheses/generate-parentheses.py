
# @Title: 括号生成 (Generate Parentheses)
# @Author: 18015528893
# @Date: 2021-02-18 11:30:44
# @Runtime: 52 ms
# @Memory: 15.1 MB

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(path, stack):
            if len(path) == 2 * n and len(stack) == 0:
                ans.append(''.join(path))

            if len(path) >= 2 * n:
                return

            if len(stack) > n:
                choices = [")"]
            elif len(stack) == 0:
                choices = ["("]
            else:
                choices = ["(", ")"]

            for choice in choices:
                path.append(choice)
                if choice == '(':
                    stack.append('(')
                else:
                    stack.pop()
                backtrack(path, stack)
                path.pop()
                if choice == '(':
                    stack.pop()
                else:
                    stack.append('(')

        backtrack([], [])
        return ans


