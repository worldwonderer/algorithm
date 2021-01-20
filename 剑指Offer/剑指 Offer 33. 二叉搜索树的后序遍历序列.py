class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j:
                return True
            m = i
            while postorder[m] < postorder[j]:
                m += 1
            n = m
            while postorder[m] > postorder[j]:
                m += 1
            return m == j and recur(i, n-1) and recur(n, j-1)
        return recur(0, len(postorder)-1)
