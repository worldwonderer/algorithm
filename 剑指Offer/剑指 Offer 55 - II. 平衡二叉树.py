class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if root is None:
                return 0
            l = recur(root.left)
            if l == -1:
                return -1
            r = recur(root.right)
            if r == -1:
                return -1

            return max(l, r) + 1 if abs(l-r) <= 1 else -1
        return recur(root) != -1
