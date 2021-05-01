
# @Title: 二叉树的锯齿形层序遍历 (Binary Tree Zigzag Level Order Traversal)
# @Author: 18015528893
# @Date: 2021-02-14 11:51:49
# @Runtime: 32 ms
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
        result = []
        q = deque()
        q.append(root)
        l2r = True
        while q:
            size = len(q)
            floor = [0] * size
            for i in range(size):
                node = q.popleft() 
                if l2r:
                    index = i
                else:
                    index = size - 1 - i
                floor[index] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l2r = not l2r
            result.append(floor)
        return result

