
# @Title: 两个链表的第一个公共节点 (两个链表的第一个公共节点  LCOF)
# @Author: 18015528893
# @Date: 2021-02-12 21:42:32
# @Runtime: 156 ms
# @Memory: 29.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p = headA
        q = headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

