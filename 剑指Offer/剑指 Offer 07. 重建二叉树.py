# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    前序遍历，根节点-左子树-右子树
    中序遍历，左子树-根节点-右子树
    1. 前序遍历的首个节点即为根节点
    2. 在中序遍历中搜索根节点，即可将中序遍历分为左子树-根节点-右子树
    3. 根据中序遍历中的左右子树节点数量，可以将前序遍历分为根节点-左子树-右子树
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.inorder_map = dict()
        self.preorder = preorder
        for i, val in enumerate(inorder):
            self.inorder_map[val] = i
        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, preorder_root_index, in_left, in_right):
        if in_left > in_right:
            return
        root = TreeNode(self.preorder[preorder_root_index])
        inorder_root_index = self.inorder_map[root.val]
        root.left = self.recur(preorder_root_index + 1, in_left, inorder_root_index - 1)
        # inorder_root_index - in_left 为左子树的长度
        root.right = self.recur(inorder_root_index - in_left + preorder_root_index + 1, inorder_root_index + 1,
                                in_right)
        return root
