
# @Title: 外观数列 (Count and Say)
# @Author: 18015528893
# @Date: 2019-10-22 12:57:48
# @Runtime: 48 ms
# @Memory: 13.6 MB

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        ret = ''
        count = 1
        last_num = None
        for num in self.countAndSay(n-1):
            if last_num is None:
                last_num = num
            else:
                if last_num == num:
                    count += 1
                else:
                    ret += str(count)
                    ret += last_num
                    last_num = num
                    count = 1
        if count != 0:
            ret += str(count)
            ret += last_num
        return ret
