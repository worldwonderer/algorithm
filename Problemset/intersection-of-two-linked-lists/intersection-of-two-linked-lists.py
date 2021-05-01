
# @Title: 相交链表 (Intersection of Two Linked Lists)
# @Author: 18015528893
# @Date: 2021-02-13 10:49:57
# @Runtime: 152 ms
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

