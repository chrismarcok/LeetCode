# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        c = 0
        while cur:
            cur = cur.next
            c += 1
        cur = head
        if n == c:
            return head.next
        for x in range(c-n-1):
            cur = cur.next
        cur.next = cur.next.next
        return head