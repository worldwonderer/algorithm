
# @Title: 从前序与中序遍历序列构造二叉树 (Construct Binary Tree from Preorder and Inorder Traversal)
# @Author: 18015528893
# @Date: 2021-02-14 16:04:22
# @Runtime: 224 ms
# @Memory: 19.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pstart, pend, istart, iend):
            if pstart > pend:
                return
            
            root_val = preorder[pstart]
            index = istart
            for i in range(istart, iend+1):
                if inorder[i] == root_val:
                    index = i
                    break
            
            left_length = index - istart
            root = TreeNode(root_val)
            root.left = build(pstart+1, pstart+left_length, istart, istart+left_length)
            root.right = build(pstart+left_length+1, pend, istart+left_length+1, iend)
            return root
        
        return build(0, len(preorder)-1, 0, len(inorder)-1)
