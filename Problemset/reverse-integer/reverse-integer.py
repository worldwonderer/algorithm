
# @Title: 整数反转 (Reverse Integer)
# @Author: 18015528893
# @Date: 2019-10-21 21:21:30
# @Runtime: 32 ms
# @Memory: 13.5 MB

class Solution:
    def reverse(self, x: int) -> int:
        max_value = (1 << 31) - 1
        min_value = -1 << 31
        ans = 0
        while x != 0:
            if x >= 0:
                p = x % 10
            else:
                p = x % 10 - 10
            if x > 0 and ans * 10 + p > max_value:
                return 0
            if x < 0 and ans * 10 + p < min_value:
                return 0
            ans *= 10
            ans += p
            x //= 10
            if x < 0:
                x += 1
            print(p, ans, x)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-321))


