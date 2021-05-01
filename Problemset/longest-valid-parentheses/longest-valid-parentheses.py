
# @Title: 最长有效括号 (Longest Valid Parentheses)
# @Author: 18015528893
# @Date: 2021-02-18 13:44:50
# @Runtime: 28 ms
# @Memory: 15 MB

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        j = -1  # j+1是上一个最长有效括号的开始索引
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    top = stack[-1] if stack else j  # 如果栈内还有多余的(，如(()，top取该(的索引，否则如)(())，取j
                    ans = max(ans, i - top)
                else:
                    j = i
        return ans

