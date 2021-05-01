
# @Title: 括号 (Bracket LCCI)
# @Author: 18015528893
# @Date: 2021-02-12 14:15:30
# @Runtime: 48 ms
# @Memory: 15.1 MB

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        result = []

        def backtrack(path, stack):
            if len(path) == 2 * n and len(stack) == 0:
                result.append(''.join(path))
            
            if len(path) >= 2 * n:
                return

            if len(stack) == 0:
                choices = ['(']
            elif len(stack) == n:
                choices = [')']
            else:
                choices = ['(', ')']

            for choice in choices:
                if choice == '(':
                    stack.append(choice)
                else:
                    stack.pop()
                path.append(choice)
                backtrack(path, stack)
                path.pop()
                if choice == '(':
                    stack.pop()
                else:
                    stack.append(choice)

        backtrack([], [])
        return result
