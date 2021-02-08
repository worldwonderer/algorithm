
# @Title: 从前序与中序遍历序列构造二叉树 (Construct Binary Tree from Preorder and Inorder Traversal)
# @Author: 18015528893
# @Date: 2021-02-08 11:17:18
# @Runtime: 228 ms
# @Memory: 19.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorder, pstart, pend, inorder, istart, iend):
            if pstart > pend:
                return

            root_val = preorder[pstart]

            index = istart
            for i in range(istart, iend+1):
                if inorder[i] == root_val:
                    index = i
                    break

            left_size = index - istart

            root = TreeNode(root_val)
            root.left = build(preorder, pstart+1, pstart+left_size, inorder, istart, index-1)
            root.right = build(preorder, pstart+left_size+1, pend, inorder, index+1, iend)
            return root

        return build(preorder, 0, len(preorder)-1,
                     inorder, 0, len(inorder)-1)











