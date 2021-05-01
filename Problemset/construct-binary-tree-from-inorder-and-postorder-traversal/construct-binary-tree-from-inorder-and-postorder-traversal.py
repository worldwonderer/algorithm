
# @Title: 从中序与后序遍历序列构造二叉树 (Construct Binary Tree from Inorder and Postorder Traversal)
# @Author: 18015528893
# @Date: 2021-02-14 21:55:50
# @Runtime: 232 ms
# @Memory: 19.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(pstart, pend, istart, iend):
            if pstart > pend:
                return
            
            root_val = postorder[pend]
            root = TreeNode(root_val)
            
            index = istart
            for i in range(istart, iend+1):
                if inorder[i] == root_val:
                    index = i
                    break
            left_length = index - istart

            root.left = build(pstart, pstart+left_length-1, istart, index-1)
            root.right = build(pstart+left_length, pend-1, index+1, iend)
            return root
        return build(0, len(inorder)-1, 0, len(inorder)-1)

