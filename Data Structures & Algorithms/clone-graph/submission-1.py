"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # old to new dict
        g = {}
        def dfs(node):
            # we want to copy every node
            # 1 if node is None
            # return None

            # 2 if node in g, it is already clone
            # return corresponding node
            if node is None:
                return None
            if node in g:
                return g[node]
            cloned = Node(node.val)
            g[node] = cloned

            for neibor in node.neighbors:
                cloned.neighbors.append(dfs(neibor))
            return cloned
        
        return dfs(node)


