
# @Title: 外观数列 (Count and Say)
# @Author: 18015528893
# @Date: 2021-02-22 00:00:40
# @Runtime: 48 ms
# @Memory: 15.1 MB

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        ans = ""
        count = 1
        last = None
        for num_str in self.countAndSay(n-1):
            if last is None:
                last = num_str
            else:
                if last == num_str:
                    count += 1
                else:
                    ans += str(count)
                    ans += last
                    last = num_str
                    count = 1
        if count != 0:
            ans += str(count)
            ans += last
        return ans

