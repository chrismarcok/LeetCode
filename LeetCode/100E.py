# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (q is None and p is not None) or (p is None and q is not None):
            return False
        if p is None and q is None:
            return True
        return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)