
# @Title: 最小的k个数 (最小的k个数  LCOF)
# @Author: 18015528893
# @Date: 2021-01-21 22:06:32
# @Runtime: 116 ms
# @Memory: 15.8 MB

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        if len(arr) <= k:
            return arr

        self.partition_helper(arr, 0, len(arr) - 1, k)
        return arr[:k]

    def partition_helper(self, arr, lo, hi, k):
        j = self.partition(arr, lo, hi)
        if j > k:
            self.partition_helper(arr, lo, j-1, k)
        elif j < k:
            self.partition_helper(arr, j+1, hi, k)

    def partition(self, arr, lo, hi):
        if lo == hi:
            return lo
        v = arr[lo]
        i = lo
        j = hi+1
        while True:
            while True:
                i += 1
                if arr[i] > v:
                    break
                if i >= hi:
                    break
            while True:
                j -= 1
                if arr[j] < v:
                    break
                if j <= lo:
                    break
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        arr[lo], arr[j] = arr[j], arr[lo]
        return j


