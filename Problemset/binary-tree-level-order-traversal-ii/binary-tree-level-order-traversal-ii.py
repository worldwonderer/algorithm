
# @Title: 二叉树的层序遍历 II (Binary Tree Level Order Traversal II)
# @Author: 18015528893
# @Date: 2021-02-14 15:55:38
# @Runtime: 44 ms
# @Memory: 15.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            floor = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                floor.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(floor)
        return res[::-1]
