
# @Title: 环形链表 (Linked List Cycle)
# @Author: 18015528893
# @Date: 2021-02-03 11:34:36
# @Runtime: 64 ms
# @Memory: 17.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    s.hasCycle(None)

