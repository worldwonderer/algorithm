class Solution:

    k = None
    res = None

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k

        def dfs(root):
            if root is None:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        dfs(root)
        return self.res
