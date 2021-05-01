
# @Title: 有效的括号 (Valid Parentheses)
# @Author: 18015528893
# @Date: 2021-02-18 11:14:01
# @Runtime: 36 ms
# @Memory: 15 MB

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        half = len(s) // 2

        stack = []
        left = set('([{')
        for char in s:
            if char in left:
                stack.append(char)
                if len(stack) > half:
                    return False
            else:
                if len(stack) == 0:
                    return False
                if char == ')' and stack[-1] != '(':
                    return False
                if char == ']' and stack[-1] != '[':
                    return False
                if char == '}' and stack[-1] != '{':
                    return False
                stack.pop()

        return len(stack) == 0


