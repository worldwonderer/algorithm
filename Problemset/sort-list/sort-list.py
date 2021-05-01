
# @Title: 排序链表 (Sort List)
# @Author: 18015528893
# @Date: 2021-02-13 11:30:38
# @Runtime: 520 ms
# @Memory: 29.9 MB

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

        def get_length(head):
            p = head
            length = 0
            while p:
                p = p.next
                length += 1
            return length

        def cut(head, n):
            p = head
            while p and n - 1 > 0:
                p = p.next
                n -= 1
            if p is None:
                return
            new_head = p.next
            p.next = None
            return new_head

        def merge(l1, l2):
            dummy = ListNode(0)
            p = dummy
            while l1 and l2:
                if l1.val < l2.val:
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

        length = get_length(head)
        i = 1
        while i < length:
            tail = dummy
            cur = dummy.next
            while cur:
                left = cur
                right = cut(left, i)
                cur = cut(right, i)
                tail.next = merge(left, right)
                while tail.next:
                    tail = tail.next
            i *= 2
        return dummy.next
