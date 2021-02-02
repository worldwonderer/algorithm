
# @Title: K 个一组翻转链表 (Reverse Nodes in k-Group)
# @Author: 18015528893
# @Date: 2021-02-02 23:04:07
# @Runtime: 56 ms
# @Memory: 15.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        a = b = head
        for i in range(k):
            if b is None:
                return head
            b = b.next

        new_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head


    def reverse(self, a, b):
        pre = None
        cur = a
        while cur != b:
            next_tmp = cur.next
            cur.next = pre
            pre = cur
            cur = next_tmp
        return pre

