
# @Title: 合并区间 (Merge Intervals)
# @Author: 18015528893
# @Date: 2021-02-23 10:46:55
# @Runtime: 48 ms
# @Memory: 15.5 MB

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            last = ans[-1]
            interval = intervals[i]
            if last[1] >= interval[0]:
                last[1] = max(last[1], interval[1])
            else:
                ans.append(interval)

        return ans





