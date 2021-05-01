
# @Title: 实现 strStr() (Implement strStr())
# @Author: 18015528893
# @Date: 2021-02-20 11:08:11
# @Runtime: 56 ms
# @Memory: 15.9 MB

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        nxt = []
        def search():
            tar = 0
            pos = 0

            while tar < len(haystack):
                if haystack[tar] == needle[pos]:
                    tar += 1
                    pos += 1
                elif pos != 0:
                    pos = nxt[pos-1]
                else:
                    tar += 1

                if pos == len(needle):
                    return tar - pos

            return -1

        def gen_nxt():
            nxt.append(0)
            x = 1
            now = 0  # next[x-1]

            while x < len(needle):
                if needle[x] == needle[now]:
                    x += 1
                    now += 1
                    nxt.append(now)
                elif now != 0:
                    now = nxt[now-1]
                else:
                    x += 1
                    nxt.append(0)

        gen_nxt()
        return search()


