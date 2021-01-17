# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy_node = ListNode(0)
        dummy_node.next = head
        if head.val == val:
            return head.next
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
                break
            head = head.next
        return dummy_node.next
