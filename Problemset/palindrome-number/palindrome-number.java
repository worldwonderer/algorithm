
// @Title: 回文数 (Palindrome Number)
// @Author: 18015528893
// @Date: 2021-02-18 18:59:21
// @Runtime: 10 ms
// @Memory: 37.9 MB

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int ans = 0;
        int i = x;
        while (i != 0) {
            if (i > 0 && ans > (Integer.MAX_VALUE - i % 10) / 10) {
                return false;
            }
            if (i < 0 && ans < (Integer.MIN_VALUE - i % 10) / 10) {
                return false;
            }
            ans = 10 * ans + i % 10;
            i /= 10;
        }
        if (x == ans) {
            return true;
        } else {
            return false;
        }
    }
}
