# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        d = {}
        cur = head
        
        while cur is not None:
            
            if cur not in d:
                d[cur] = True
            else:
                return True
            cur = cur.next
        
        return False