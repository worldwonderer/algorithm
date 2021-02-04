
# @Title: 删除中间节点 (Delete Middle Node LCCI)
# @Author: 18015528893
# @Date: 2021-02-04 23:06:52
# @Runtime: 44 ms
# @Memory: 15.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        

