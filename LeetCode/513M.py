# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = self.getDepth(root, 0)
        
        result = self.getLeft(root, 0, depth, 0)
        result = [x for x in result if x != []]
        new_list = sorted(result, key=lambda x: x[1])
        return new_list[-1][0]
        
    def getLeft(self, root, depth, target_d, leftness):
        if root.left is None and root.right is None:
            if (depth == target_d):
                return [[root.val, leftness]]
            else:
                return [[]]
        elif root.left is None: # goign right
            return self.getLeft(root.right, depth + 1, target_d, leftness - 1)
        elif root.right is None:
            return self.getLeft(root.left, depth + 1, target_d, leftness + 1)
        else:
            return self.getLeft(root.right, depth + 1, target_d, leftness - 1) + self.getLeft(root.left, depth + 1, target_d, leftness + 1)
        
    def getDepth(self, root, d):
        if root.left is None and root.right is None:
            return d
        elif root.left is None:
            return self.getDepth(root.right, d + 1)
        elif root.right is None:
            return self.getDepth(root.left, d + 1)
        else:
            return max(self.getDepth(root.left, d + 1), self.getDepth(root.right, d + 1))