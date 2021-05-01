
# @Title: 二叉树的右视图 (Binary Tree Right Side View)
# @Author: 18015528893
# @Date: 2021-02-14 17:44:38
# @Runtime: 44 ms
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
        result = []
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            last = None
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    last = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(last)
        return result

