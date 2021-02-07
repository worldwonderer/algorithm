
# @Title: 二叉树的右视图 (Binary Tree Right Side View)
# @Author: 18015528893
# @Date: 2021-02-07 10:55:53
# @Runtime: 40 ms
# @Memory: 14.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res = []
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            floor = []
            for i in range(size):
                node = q.popleft()
                if node:
                    floor.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if floor:
                res.append(floor[-1])
        return res


