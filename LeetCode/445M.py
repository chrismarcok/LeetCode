# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        num1, num2 = "", ""
        
        cur = l1
        while cur != None:
            num1 += str(cur.val)
            cur = cur.next
        cur = l2
        while cur != None:
            num2 += str(cur.val)
            cur = cur.next
        sumString = str(int(num1) + int(num2))
        
        
        prev = ListNode(int(sumString[0]))
        head = prev
        for x in range(1, len(sumString)):
            cur = ListNode(int(sumString[x]))
            prev.next = cur
            prev = prev.next
        return head