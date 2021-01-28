
# @Title: 栈的压入、弹出序列 (栈的压入、弹出序列 LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 21:33:17
# @Runtime: 60 ms
# @Memory: 15.1 MB

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = list()
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return len(stack) == 0


