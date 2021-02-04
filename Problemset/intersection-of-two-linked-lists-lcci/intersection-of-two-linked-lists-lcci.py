
# @Title: 链表相交 (Intersection of Two Linked Lists LCCI)
# @Author: 18015528893
# @Date: 2021-02-04 23:12:52
# @Runtime: 184 ms
# @Memory: 29.7 MB

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
        

