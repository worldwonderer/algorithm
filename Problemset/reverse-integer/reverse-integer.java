
// @Title: 整数反转 (Reverse Integer)
// @Author: 18015528893
// @Date: 2021-02-18 18:24:24
// @Runtime: 1 ms
// @Memory: 35.6 MB

class Solution {
    public int reverse(int x) {
        int ans = 0;
        while (x != 0) {
            if (x > 0 && ans > (Integer.MAX_VALUE - x % 10) / 10) return 0;
            if (x < 0 && ans < (Integer.MIN_VALUE - x % 10) / 10) return 0;
            ans = ans * 10 + x % 10;
            x /= 10;
        }
        return ans;
    }
}
