"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}

        def dfs(node):
            if node is None:
                return None
            if node in visited:
                return visited[node]

            copy = Node(node.val, None, None)
            visited[node] = copy
            copy.next = dfs(node.next)
            copy.random = dfs(node.random)
            return copy

        return dfs(head)
