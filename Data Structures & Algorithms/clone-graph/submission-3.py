"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        g = {}

        def dfs(node):
            # return the cloned node for node
            if node in g:
                return g[node]

            cloned = Node(node.val)
            g[node] = cloned

            for nxt in node.neighbors:
                cloned.neighbors.append(dfs(nxt))
            return cloned
        return dfs(node)
            