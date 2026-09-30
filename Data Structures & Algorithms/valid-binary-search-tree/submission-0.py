# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # given root, return True if it is a valid BST
        # BST: all val in left subtree < node < all val in right subtree

        def dfs(node, min_val, max_val) -> bool:
            # helper func to determine if BST constraint hold
            # base case
            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False
            
            left_is_good = dfs(node.left, min_val, max_val)
            right_is_good = dfs(node.right, min_val, max_val)

            return left_is_good and right_is_good
        
        return dfs(root, float("-inf"), float("inf"))
