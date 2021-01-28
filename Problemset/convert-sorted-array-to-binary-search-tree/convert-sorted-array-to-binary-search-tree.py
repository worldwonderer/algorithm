
# @Title: 将有序数组转换为二叉搜索树 (Convert Sorted Array to Binary Search Tree)
# @Author: 18015528893
# @Date: 2019-10-24 23:42:18
# @Runtime: 80 ms
# @Memory: 15.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        lo = 0
        hi = len(nums) - 1
        mid = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
