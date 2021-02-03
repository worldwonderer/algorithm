
# @Title: 删除链表的倒数第 N 个结点 (Remove Nth Node From End of List)
# @Author: 18015528893
# @Date: 2021-02-03 11:22:57
# @Runtime: 40 ms
# @Memory: 14.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        fast = head
        slow = dummy

        for i in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


