# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        lstA, lstB =[],[]
        curA = headA
        curB = headB
        while curA or curB:
            if curA:
                lstA.append(curA)
                curA = curA.next
            if curB:
                lstB.append(curB)
                curB = curB.next
        lstA.reverse()
        lstB.reverse()
        x = 0
        while lstA[x] is lstB[x]:
            x += 1
            if x >= len(lstA) or x >= len(lstB):
                return lstA[x-1]
        return lstA[x-1] if x != 0 else None