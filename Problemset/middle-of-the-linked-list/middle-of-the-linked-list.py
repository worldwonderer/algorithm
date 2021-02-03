
# @Title: 链表的中间结点 (Middle of the Linked List)
# @Author: 18015528893
# @Date: 2021-02-03 14:10:44
# @Runtime: 32 ms
# @Memory: 14.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        

