
# @Title: 删除被覆盖区间 (Remove Covered Intervals)
# @Author: 18015528893
# @Date: 2021-02-22 22:47:48
# @Runtime: 56 ms
# @Memory: 15.3 MB

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1], reverse=True)
        intervals.sort(key=lambda x: x[0])
        print(intervals)

        left = intervals[0][0]
        right = intervals[0][1]

        ans = 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= left and interval[1] <= right:
                ans += 1
            if interval[0] <= right and interval[1] >= right:
                right = interval[1]
            if interval[0] > right:
                left = interval[0]
                right = interval[1]
        return len(intervals) - ans
 
