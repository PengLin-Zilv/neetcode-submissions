# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case
        # if subRoot is null, return True
        if not subRoot:
            return True

        # if subRoot has value but root is gone, return False
        if not root:
            return False
        
        # if both has value
        if self.isSametree(root, subRoot):
            return True
        
        # recursive call, see if children is the same with subRoot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSametree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case
        # if subroot is gone or root is gone
        if not subRoot and not root:
            return True

        if root and not subRoot:
            return False
        if subRoot and not root:
            return False

        if root.val == subRoot.val:
            return self.isSametree(root.left, subRoot.left) and self.isSametree(root.right, subRoot.right)
