# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        cur = head
        i = 1
        swapsMade = 0
        while cur != None:
            if m <= i <= n:
                
                temp = cur
                for x in range(i, n - swapsMade):
                    temp = temp.next
                #now temp should be ready to swap with whatever
                temp.val, cur.val = cur.val, temp.val
                swapsMade += 1
            cur = cur.next
            i += 1
            
        return head