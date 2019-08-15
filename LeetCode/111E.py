# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.helper(root, 1)
        
    def helper(self, root, depth):
        if root.left is None and root.right is None:
            return depth
        if root.left is None:
            return self.helper(root.right, depth + 1)
        if root.right is None:
            return self.helper(root.left, depth + 1)
        else:
            return min(self.helper(root.left, depth + 1), self.helper(root.right, depth + 1))