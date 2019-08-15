# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, f: int) -> bool:
        if not root:
            return 0
        q = [[root, root.val]]
        while q:
            t=q.pop()
            node, val = t[0], t[1]
            
            if not node.left and not node.right:
                if val == f:
                    return True
            if node.left:
                q.append([node.left, val + node.left.val])
            if node.right:
                q.append([node.right, val + node.right.val])
        return False