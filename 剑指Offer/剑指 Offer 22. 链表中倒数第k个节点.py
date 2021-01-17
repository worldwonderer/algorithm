class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = head
        slow = head
        for _ in range(k):
            if fast is None:
                return
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
