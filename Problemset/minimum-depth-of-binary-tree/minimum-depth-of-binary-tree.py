
# @Title: 二叉树的最小深度 (Minimum Depth of Binary Tree)
# @Author: 18015528893
# @Date: 2021-02-14 21:36:03
# @Runtime: 480 ms
# @Memory: 51.7 MB

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
        floor = 1
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return floor
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            floor += 1

