
# @Title: 分割链表 (Partition List LCCI)
# @Author: 18015528893
# @Date: 2021-02-04 22:59:09
# @Runtime: 32 ms
# @Memory: 14.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = ListNode(0)
        right = ListNode(0)
        p = left
        q = right
        while head:
            tmp = head.next
            head.next = None
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = tmp
        left.next = q.next
        return p.next


