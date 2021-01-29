
# @Title: 队列的最大值 (队列的最大值 LCOF)
# @Author: 18015528893
# @Date: 2021-01-29 23:39:25
# @Runtime: 404 ms
# @Memory: 18.5 MB

from queue import Queue
from collections import deque

class MaxQueue:

    def __init__(self):
        self.q = Queue()
        self.s = deque()

    def max_value(self) -> int:
        return self.s[0] if self.s else -1

    def push_back(self, value: int) -> None:
        self.q.put(value)
        while self.s and self.s[-1] < value:
            self.s.pop()
        self.s.append(value)

    def pop_front(self) -> int:
        if self.q.empty():
            return -1
        value = self.q.get()
        if value == self.s[0]:
            self.s.popleft()
        return value

