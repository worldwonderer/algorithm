
# @Title: 完全二叉树的节点个数 (Count Complete Tree Nodes)
# @Author: 18015528893
# @Date: 2021-02-14 15:41:05
# @Runtime: 80 ms
# @Memory: 21.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def get_height(root):
            if root is None:
                return 0
            return get_height(root.left) + 1

        height = get_height(root)
        if height <= 1:
            return height
        if get_height(root.right) == height - 2:
            return (1 << (height - 2)) + self.countNodes(root.left)
        else:
            return (1 << (height - 1)) + self.countNodes(root.right)

