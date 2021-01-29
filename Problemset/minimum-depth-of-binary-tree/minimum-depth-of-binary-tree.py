
# @Title: 二叉树的最小深度 (Minimum Depth of Binary Tree)
# @Author: 18015528893
# @Date: 2021-01-29 11:21:55
# @Runtime: 596 ms
# @Memory: 51.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque()
        q.append(root)
        depth = 1
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node:
                    if node.left is None and node.right is None:
                        return depth
                    q.append(node.left)
                    q.append(node.right)
            depth += 1


