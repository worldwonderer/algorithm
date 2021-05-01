
# @Title: 反转链表 II (Reverse Linked List II)
# @Author: 18015528893
# @Date: 2021-02-12 15:10:10
# @Runtime: 40 ms
# @Memory: 15.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        successor = None
        def reverseN(head, n):
            global successor
            if n == 1:
                successor = head.next
                return head
            pre = reverseN(head.next, n-1)
            head.next.next = head
            head.next = successor
            return pre

        if m == 1:
            return reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head
            
