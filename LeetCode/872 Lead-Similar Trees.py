# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafOrder(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        else:
            return sum([],
                       self.leafOrder(root.left) + self.leafOrder(root.right))

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leafOrder(root1) == self.leafOrder(root2)
