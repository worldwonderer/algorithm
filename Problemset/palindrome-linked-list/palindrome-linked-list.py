
# @Title: 回文链表 (Palindrome Linked List)
# @Author: 18015528893
# @Date: 2021-02-12 21:29:36
# @Runtime: 76 ms
# @Memory: 24.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next
        if f is not None:
            s = s.next
        
        def reverse(head):
            pre = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        
        right = reverse(s)
        left = head
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next

        return True
        

