
# @Title: 删除链表的节点 (删除链表的节点 LCOF)
# @Author: 18015528893
# @Date: 2021-02-13 15:46:55
# @Runtime: 48 ms
# @Memory: 15.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            if cur.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
            cur = pre.next
        return dummy.next

