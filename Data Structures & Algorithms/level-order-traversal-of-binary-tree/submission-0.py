# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # use bfs to return each layer
        result = []

        # we want their left children and right children
        # and for their left children and right children, we want each of their left and right children
        # we want to use recursion, but we want a condition to check if the layer is finished

        queue = deque([root])

        while queue:
            level_length = len(queue)
            level_list = []

            for _ in range(level_length):
                node = queue.popleft()
                level_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_list)
        return result



        