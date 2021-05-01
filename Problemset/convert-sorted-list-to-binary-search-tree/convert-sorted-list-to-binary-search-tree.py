
# @Title: 有序链表转换二叉搜索树 (Convert Sorted List to Binary Search Tree)
# @Author: 18015528893
# @Date: 2021-02-13 13:38:15
# @Runtime: 80 ms
# @Memory: 17.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)

        f = head
        s = head
        pre = None
        while f and f.next:
            f = f.next.next
            pre = s
            s = s.next
        pre.next = None
        right = s.next
        root = TreeNode(s.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right)
        return root

