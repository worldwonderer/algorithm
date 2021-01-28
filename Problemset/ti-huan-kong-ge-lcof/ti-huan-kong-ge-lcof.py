
# @Title: 替换空格 (替换空格 LCOF)
# @Author: 18015528893
# @Date: 2020-09-15 22:05:09
# @Runtime: 32 ms
# @Memory: 13.2 MB

class Solution:
    """
    首先遍历一次字符串s来统计有多少个空格
    假设有m个空格，我们需要填充的%20占用三个字符位置，所以需要额外开辟出2*m个空间
    将开辟出的空间链接到原字符串的后面，新的字符串命名为s_new设置两个指针p1和p2，初始时p1指向原字符串s的末尾，p2指向s_new的末尾
    p1指针向前移动，当p1指向的字符不是空格时，将p1指向的字符复制到p2指向的位置，并都向前移动一位
    当p1指向的字符是空格时，p1向前移动一格，这时应该插入%20，所以p2向前移动三格，并在这三格中插入%，2，0
    时间复杂度O(n)，空间复杂度O(n+2m)

    """
    def replaceSpace(self, s: str) -> str:
        m = 0
        l = len(s)
        for i in s:
            if i == ' ':
                m += 1
        resized = list(s) + [''] * (2*m)
        p1 = l - 1
        p2 = l + 2*m - 1
        while p1 >= 0:
            if resized[p1] != ' ':
                resized[p2] = resized[p1]
                p1 -= 1
                p2 -= 1
            else:
                for i in '02%':
                    resized[p2] = i
                    p2 -= 1
                p1 -= 1
        return ''.join(resized)

