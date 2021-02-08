
# @Title: 左叶子之和 (Sum of Left Leaves)
# @Author: 18015528893
# @Date: 2021-02-08 12:24:37
# @Runtime: 40 ms
# @Memory: 15.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = deque()
        q.append((root, False))
        s = 0

        while q:
            size = len(q)
            for _ in range(size):
                node, is_left = q.popleft()
                if node:
                    if is_left and node.left is None and node.right is None:
                        s += node.val
                    q.append((node.left, True))
                    q.append((node.right, False))
        return s


        

