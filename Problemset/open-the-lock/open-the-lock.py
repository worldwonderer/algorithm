
# @Title: 打开转盘锁 (Open the Lock)
# @Author: 18015528893
# @Date: 2021-01-29 11:55:03
# @Runtime: 864 ms
# @Memory: 15.8 MB

from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def up(s, i):
            arr = list(s)
            if arr[i] == '9':
                arr[i] = '0'
            else:
                arr[i] = str(int(arr[i]) + 1)
            return ''.join(arr)

        def down(s, i):
            arr = list(s)
            if arr[i] == '0':
                arr[i] = '9'
            else:
                arr[i] = str(int(arr[i]) - 1)
            return ''.join(arr)

        q = deque()
        visited = set(deadends)
        if '0000' in visited:
            return -1
        q.append("0000")
        visited.add("0000")
        count = 0
        while q:
            size = len(q)
            for _ in range(size):
                s = q.popleft()
                if s == target:
                    return count
                for i in range(4):
                    for func in (up, down):
                        n = func(s, i)
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            count += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.openLock(["0201","0101","0102","1212","2002"], '0202'))

