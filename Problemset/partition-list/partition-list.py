
# @Title: 分隔链表 (Partition List)
# @Author: 18015528893
# @Date: 2021-02-03 17:29:40
# @Runtime: 44 ms
# @Memory: 15 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        i = ListNode()
        j = ListNode()
        head_j = j
        head_i = i
        while head:
            if head.val < x:
                i.next = ListNode(head.val)
                i = i.next
            else:
                j.next = ListNode(head.val)
                j = j.next
            head = head.next
        i.next = head_j.next
        return head_i.next


