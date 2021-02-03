
# @Title: 有序链表转换二叉搜索树 (Convert Sorted List to Binary Search Tree)
# @Author: 18015528893
# @Date: 2021-02-03 18:39:49
# @Runtime: 80 ms
# @Memory: 20.9 MB

class Solution:
    def sortedListToBST(self, head) -> TreeNode:
        arr = []
        if head is None:
            return None

        def buildBSTree(lo, hi):
            if lo > hi:
                return
            mid = lo + (hi - lo) // 2
            root = TreeNode(arr[mid])
            root.left = buildBSTree(lo, mid-1)
            root.right = buildBSTree(mid+1, hi)
            return root

        while head:
            arr.append(head.val)
            head = head.next
        return buildBSTree(0, len(arr)-1)
