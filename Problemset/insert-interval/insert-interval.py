
# @Title: 插入区间 (Insert Interval)
# @Author: 18015528893
# @Date: 2021-02-23 11:07:36
# @Runtime: 52 ms
# @Memory: 16.3 MB

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        ans.append(newInterval)

        while i < len(intervals):
            ans.append(intervals[i])
            i += 1

        return ans


