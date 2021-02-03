
# @Title: 旋转链表 (Rotate List)
# @Author: 18015528893
# @Date: 2021-02-03 15:53:27
# @Runtime: 44 ms
# @Memory: 14.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return

        q = head
        length = 1
        while q.next:
            q = q.next
            length += 1
        q.next = head  # 链表成环

        k = length - k % length  # 移动前length - k % length个node
        p = head
        for _ in range(k-1):
            p = p.next
        new_head = p.next
        p.next = None
        return new_head


