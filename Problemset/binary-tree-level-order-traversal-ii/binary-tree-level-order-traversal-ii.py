
# @Title: 二叉树的层序遍历 II (Binary Tree Level Order Traversal II)
# @Author: 18015528893
# @Date: 2019-10-24 23:31:04
# @Runtime: 48 ms
# @Memory: 13.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return list()
        ret = list()
        queue = list()
        queue.append(root)
        while queue:
            size = len(queue)
            row = list()
            while size > 0:
                n = queue.pop(0)
                size -= 1
                row.append(n.val)
                
                if n.left is not None:
                    queue.append(n.left)
                if n.right is not None:
                    queue.append(n.right)
            ret.append(row)
        return ret[::-1]
