
# @Title: 回文链表 (Palindrome Linked List)
# @Author: 18015528893
# @Date: 2021-02-02 23:21:34
# @Runtime: 80 ms
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
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        left = head
        right = self.reverse(slow)

        while right:
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        return True

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            next_tmp = cur.next
            cur.next = pre
            pre = cur
            cur = next_tmp
        return pre


