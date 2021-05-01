
# @Title: 简化路径 (Simplify Path)
# @Author: 18015528893
# @Date: 2021-02-24 10:22:52
# @Runtime: 32 ms
# @Memory: 15.1 MB



class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for s in path.split('/'):
            if s == '.' or s == '':
                continue
            elif s == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return '/' + '/'.join(stack)


