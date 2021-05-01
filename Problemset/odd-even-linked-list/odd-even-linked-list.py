
# @Title: 奇偶链表 (Odd Even Linked List)
# @Author: 18015528893
# @Date: 2021-02-13 12:02:13
# @Runtime: 56 ms
# @Memory: 16.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy_left = ListNode(next=head)
        dummy_right = ListNode()
        p = dummy_right

        pre = dummy_left
        cur = head
        odd = True
        while cur:
            if odd:
                pre = pre.next
                odd = False
            else:
                pre.next = cur.next
                cur.next = None
                p.next = cur
                p = p.next
                odd = True
            cur = pre.next
        pre.next = dummy_right.next
        return dummy_left.next

