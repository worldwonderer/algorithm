
# @Title: 字符串转换整数 (atoi) (String to Integer (atoi))
# @Author: 18015528893
# @Date: 2021-02-18 18:49:53
# @Runtime: 36 ms
# @Memory: 14.9 MB

class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            else:
                break

        if i == n:
            return 0

        if s[i] == '-':
            i += 1
            sign = -1
        elif s[i] == '+':
            i += 1
            sign = 1
        else:
            sign = 1

        ans = 0
        max_value = (1 << 31) - 1
        min_value = -1 << 31
        while i < n:
            if ord('0') <= ord(s[i]) <= ord('9'):
                k = ord(s[i]) - ord('0')
                print(ans, (min_value - k) // 10)

                if sign > 0 and ans > (max_value - sign * k) // 10:
                    return max_value
                if sign < 0 and ans < (min_value - sign * k) // 10 + 1:
                    return min_value

                ans = ans * 10 + sign * k
                i += 1
            else:
                break
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("-2147483649"))

