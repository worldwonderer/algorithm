
# @Title: 两个链表的第一个公共节点 (两个链表的第一个公共节点  LCOF)
# @Author: 18015528893
# @Date: 2021-01-27 14:32:48
# @Runtime: 204 ms
# @Memory: 29.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1
        

