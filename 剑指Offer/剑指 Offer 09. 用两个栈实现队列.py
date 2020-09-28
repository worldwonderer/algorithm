class CQueue:

    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def appendTail(self, value: int) -> None:
        """
        每次往stack1
        :param value:
        :return:
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def deleteHead(self) -> int:
        if not self.stack1:
            return -1
        return self.stack1.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
