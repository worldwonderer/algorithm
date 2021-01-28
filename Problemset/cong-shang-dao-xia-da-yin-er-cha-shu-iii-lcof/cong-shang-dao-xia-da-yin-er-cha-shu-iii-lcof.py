
# @Title: 从上到下打印二叉树 III (从上到下打印二叉树 III LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 21:44:16
# @Runtime: 44 ms
# @Memory: 15.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.popleft()
                if node:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if tmp:
                if len(res) % 2 == 0:
                    res.append(tmp)
                else:
                    res.append(tmp[::-1])
        return res


