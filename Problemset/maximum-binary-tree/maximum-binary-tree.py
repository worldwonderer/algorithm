
# @Title: 最大二叉树 (Maximum Binary Tree)
# @Author: 18015528893
# @Date: 2021-02-06 10:24:28
# @Runtime: 168 ms
# @Memory: 15.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def helper(lo, hi):
            if lo > hi:
                return
            max_value = nums[hi]
            index = hi
            for i in range(lo, hi):
                if nums[i] > max_value:
                    max_value = nums[i]
                    index = i

            root = TreeNode(max_value)
            root.left = helper(lo, index-1)
            root.right = helper(index+1, hi)
            return root

        return helper(0, len(nums)-1)

