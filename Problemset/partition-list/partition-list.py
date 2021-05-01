
# @Title: 分隔链表 (Partition List)
# @Author: 18015528893
# @Date: 2021-02-13 11:56:58
# @Runtime: 44 ms
# @Memory: 15 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_left = ListNode(next=head)
        dummy_right = ListNode()
        p = dummy_right

        pre = dummy_left
        cur = dummy_left.next
        while cur:
            if cur.val >= x:
                pre.next = cur.next
                cur.next = None
                p.next = cur
                p = p.next
            else:
                pre = pre.next
            cur = pre.next
        pre.next = dummy_right.next
        return dummy_left.next

