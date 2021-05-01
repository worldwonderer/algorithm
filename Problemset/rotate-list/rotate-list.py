
# @Title: 旋转链表 (Rotate List)
# @Author: 18015528893
# @Date: 2021-02-23 22:02:11
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
        
        p = head
        length = 1 
        while p.next:
            length += 1
            p = p.next

        if k % length == 0:
            return head
    
        p.next = head

        step = length - k % length
        p = head
        for i in range(step-1):
            p = p.next
        new_head = p.next
        p.next = None
        return new_head

