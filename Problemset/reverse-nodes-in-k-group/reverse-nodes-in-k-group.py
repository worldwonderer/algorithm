
# @Title: K 个一组翻转链表 (Reverse Nodes in k-Group)
# @Author: 18015528893
# @Date: 2021-02-19 22:23:56
# @Runtime: 48 ms
# @Memory: 15.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return

        a = b = head
        for i in range(k):
            if b is None: return head
            b = b.next

        def reverse(a, b):
            pre = None
            cur = a
            while cur != b:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        
        new_head = reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head

