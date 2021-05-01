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

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

if __name__ == '__main__':
    s = MaxQueue()
    s.pop_front()
    s.push_back(15)
    s.push_back(9)