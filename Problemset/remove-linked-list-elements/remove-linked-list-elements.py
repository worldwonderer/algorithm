
# @Title: 移除链表元素 (Remove Linked List Elements)
# @Author: 18015528893
# @Date: 2021-02-13 12:50:03
# @Runtime: 64 ms
# @Memory: 17.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        pre = dummy
        cur = head
        while cur:
            if cur.val != val:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = pre.next
        return dummy.next

