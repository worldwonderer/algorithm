
# @Title: 环形链表 II (Linked List Cycle II)
# @Author: 18015528893
# @Date: 2021-02-03 22:07:59
# @Runtime: 52 ms
# @Memory: 17.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 链表头部到链表入口由a个节点，链表环有b个节点
        # f = 2s 快指针走过的节点是慢指针的两倍
        # f = s + nb 快指针比慢指针多走了n个链表环长度
        # 所以 s = nb
        # k = a + nb 从链表头走到环入口的步数
        # 所以慢指针再走a步即可
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


