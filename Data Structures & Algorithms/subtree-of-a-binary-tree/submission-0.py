# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case for subtree

        if not subRoot: # if subRoot is empty, it will be 100% subtree
            return True

        if not root:  # if root is empty, the only case it has sub tree is that sub tree is empty
        # but we already set if condition last time, so here is false
            return False

        if self.sameTree(root, subRoot):
            return True
        # if same tree, then it is subtree
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # if same tree: ideal ending of recursion will be
        # 1) root and subRoot empty for the same step

        # base cases, at the end of recursion
        if not root and not subRoot: # if both are none
            return True
        if not root or not subRoot: # if one of them is none
            return False

        # recursive condition, if they both exist, check their val
        # recursively check left, and right
        # return true if both left and right child are same

        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        