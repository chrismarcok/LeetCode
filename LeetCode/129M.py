# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, t: TreeNode) -> int:
        if t is None:
            return 0
        num = 0
        q = [(t, t.val)]
        while q:
            node = q.pop()
            
            if node[0].left and node[0].right:
                q.append((node[0].left, 10*node[1] + node[0].left.val))
                q.append((node[0].right, 10*node[1] + node[0].right.val))
            elif node[0].left:
                q.append((node[0].left, 10*node[1] + node[0].left.val))
            elif node[0].right:
                q.append((node[0].right, 10*node[1] + node[0].right.val))
            else:
                #we are a leaf!
                num += node[1]
        return num
    