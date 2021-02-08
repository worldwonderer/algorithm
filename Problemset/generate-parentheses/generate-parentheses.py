
# @Title: 括号生成 (Generate Parentheses)
# @Author: 18015528893
# @Date: 2021-02-08 16:05:35
# @Runtime: 56 ms
# @Memory: 15.3 MB

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(track, stack):
            if len(track) == 2 * n:
                if len(stack) == 0:
                    result.append(''.join(track))
                return

            if len(stack) == 0:
                choices = ['(']
            elif len(stack) >= n:
                choices = [')']
            else:
                choices = ['(', ')']
            for choice in choices:
                if choice == ')':
                    stack.pop()
                else:
                    stack.append('(')
                track.append(choice)
                backtrack(track, stack)
                track.pop()
                if choice == ')':
                    stack.append('(')
                else:
                    stack.pop()

        if n == 0:
            return []
        backtrack([], [])
        return result

