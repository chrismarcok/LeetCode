# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.helper(root, "")
    
    def helper(self, root, value):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return int(value + str(root.val), 2)
        if root.left is None:
            return self.helper(root.right, value + str(root.val))
        if root.right is None:
            return self.helper(root.left, value + str(root.val))
        else:
            return self.helper(root.left, value + str(root.val)) + self.helper(root.right, value + str(root.val))
        
            
            