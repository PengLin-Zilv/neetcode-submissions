# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # for lcs, in a BST
        # BST means, left child < root node < right child

        parent = root

        # two cases
        # a) parent is the node
        # b) parent is q or q themselve

        while root:
            if p.val < parent.val and q.val < parent.val:
                # they both on the left
                parent = parent.left
                # change parent to the left child

            elif p.val > parent.val and q.val > parent.val:
                # they both on the right side
                parent = parent.right
            else:
                # if not both on left, and not both on right, means separate, means parent is the LCA
                return parent