
# @Title: 回文链表 (Palindrome Linked List LCCI)
# @Author: 18015528893
# @Date: 2021-02-04 23:22:02
# @Runtime: 92 ms
# @Memory: 24.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        f = s = head
        while f and f.next:
            f = f.next.next
            s = s.next
        if f:
            s = s.next
        s = self.reverse(s)
        while s:
            if head.val != s.val:
                return False
            head = head.next
            s = s.next
        return True

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


