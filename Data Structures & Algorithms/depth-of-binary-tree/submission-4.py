# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case: if root is None, return 0
        if root == None:
            return 0

        left_height = 1 + self.maxDepth(root.left)
        right_height = 1 + self.maxDepth(root.right)

        return max(left_height, right_height)
        