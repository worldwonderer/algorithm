
# @Title: 奇偶链表 (Odd Even Linked List)
# @Author: 18015528893
# @Date: 2021-02-04 22:24:48
# @Runtime: 52 ms
# @Memory: 16.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        odd_head = ListNode()
        even_head = ListNode()
        o = odd_head
        e = even_head
        odd = True
        cur = head
        while cur:
            if odd:
                tmp = cur.next
                cur.next = None
                o.next = cur
                o = o.next
                cur = tmp
                odd = False
            else:
                tmp = cur.next
                cur.next = None
                e.next = cur
                e = e.next
                cur = tmp
                odd = True
        o.next = even_head.next
        return odd_head.next


