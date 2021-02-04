
# @Title: 排序链表 (Sort List)
# @Author: 18015528893
# @Date: 2021-02-04 18:16:19
# @Runtime: 516 ms
# @Memory: 30.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        dummy = ListNode(next=head)
        length = self.get_length(head)
        i = 1
        while i < length:
            cur = dummy.next
            tail = dummy
            while cur:
                left = cur
                right = self.cut(left, i)
                cur = self.cut(right, i)
                tail.next = self.merge(left, right)
                while tail.next:
                    tail = tail.next
            i *= 2
        return dummy.next

    def get_length(self, head):
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        return length

    def merge(self, l1, l2):
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next

    def cut(self, head, n):
        p = head
        while n - 1 > 0 and p:
            p = p.next
            n -= 1
        if p is None:
            return
        n = p.next
        p.next = None
        return n


