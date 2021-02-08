
# @Title: 从中序与后序遍历序列构造二叉树 (Construct Binary Tree from Inorder and Postorder Traversal)
# @Author: 18015528893
# @Date: 2021-02-08 11:28:23
# @Runtime: 276 ms
# @Memory: 19.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(inorder, istart, iend, postorder, pstart, pend):
            if pstart > pend:
                return

            root_val = postorder[pend]

            index = istart
            for i in range(istart, iend+1):
                if root_val == inorder[i]:
                    index = i
                    break

            left_size = index - istart

            root = TreeNode(root_val)
            root.left = build(
                inorder, istart, index - 1,
                postorder, pstart, pstart+left_size-1
            )
            root.right = build(
                inorder, index+1, iend,
                postorder, pstart+left_size, pend-1,
            )
            return root

        return build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)



