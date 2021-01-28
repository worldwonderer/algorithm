
# @Title: 包含min函数的栈 (包含min函数的栈 LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 21:25:21
# @Runtime: 60 ms
# @Memory: 17.9 MB

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = list()
        self.support_stack = list()

    def push(self, x: int) -> None:
        self.main_stack.append(x)
        if len(self.support_stack) == 0 or x <= self.support_stack[-1]:
            self.support_stack.append(x)

    def pop(self) -> None:
        if self.main_stack.pop() == self.support_stack[-1]:
            self.support_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def min(self) -> int:
        return self.support_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

