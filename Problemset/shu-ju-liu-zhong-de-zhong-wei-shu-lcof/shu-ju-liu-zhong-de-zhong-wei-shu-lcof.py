
# @Title: 数据流中的中位数 (数据流中的中位数  LCOF)
# @Author: 18015528893
# @Date: 2021-01-21 22:25:58
# @Runtime: 212 ms
# @Memory: 25.5 MB

from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

