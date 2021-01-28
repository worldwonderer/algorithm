
# @Title: 数组中的逆序对 (数组中的逆序对  LCOF)
# @Author: 18015528893
# @Date: 2021-01-27 14:21:31
# @Runtime: 1776 ms
# @Memory: 20 MB

from typing import List


class Solution:
    result = 0

    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        if N == 1:
            return 0
        self.merge_count([0]*N, nums, 0, N-1)
        return self.result

    def merge_count(self, aux, a, lo, hi):
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        self.merge_count(aux, a, lo, mid)
        self.merge_count(aux, a, mid+1, hi)
        self.merge(aux, a, lo, mid, hi)

    def merge(self, aux, a, lo, mid, hi):
        i = lo
        j = mid + 1
        for k in range(lo, hi + 1):
            aux[k] = a[k]
        for k in range(lo, hi + 1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                a[k] = aux[j]
                j += 1
                self.result += mid-i+1
            else:
                a[k] = aux[i]
                i += 1

if __name__ == '__main__':
    s = Solution()
    print(s.reversePairs([7,5,6,4]))


