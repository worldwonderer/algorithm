
# @Title: 链表中倒数第k个节点 (链表中倒数第k个节点 LCOF)
# @Author: 18015528893
# @Date: 2021-01-17 22:29:01
# @Runtime: 32 ms
# @Memory: 14.9 MB

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

