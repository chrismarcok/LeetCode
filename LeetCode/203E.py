# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        while head is not None and head.val == val:
            head = head.next
                
        prev = None
        cur = head
        
        while cur != None:
            deleted = False
            if cur.val == val:
                prev.next = cur.next
                deleted = True
            if (not deleted):               
                prev = cur
            cur = cur.next
        
        return head