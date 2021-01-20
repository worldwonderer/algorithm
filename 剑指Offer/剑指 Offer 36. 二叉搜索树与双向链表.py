"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:

    def __init__(self):
        self.pre = None
        self.head = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if cur is None:
                return
            dfs(cur.left)
            if self.pre is None:
                self.head = cur
            else:
                self.pre.right = cur
                cur.left = self.pre
            self.pre = cur
            dfs(cur.right)

        if root is None:
            return
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
