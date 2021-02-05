
# @Title: 二叉树的锯齿形层序遍历 (Binary Tree Zigzag Level Order Traversal)
# @Author: 18015528893
# @Date: 2021-02-05 23:03:12
# @Runtime: 40 ms
# @Memory: 15.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            floor = []
            for _ in range(size):
                node = q.popleft()
                if node:
                    floor.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if floor:
                if len(res) % 2 == 1:
                    floor = floor[::-1]
                res.append(floor)
        return res


