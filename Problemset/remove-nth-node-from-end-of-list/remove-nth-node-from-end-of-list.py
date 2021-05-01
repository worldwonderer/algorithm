
# @Title: 删除链表的倒数第 N 个结点 (Remove Nth Node From End of List)
# @Author: 18015528893
# @Date: 2021-02-18 11:21:56
# @Runtime: 44 ms
# @Memory: 14.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head

        f = s = head
        for _ in range(n):
            f = f.next

        if f is None:
            return head.next

        while f.next:
            f = f.next
            s = s.next

        s.next = s.next.next
        return head


