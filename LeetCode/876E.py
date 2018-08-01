# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        num = self.getLength(head) // 2
        curNode = head
        for x in range(num):
            curNode = curNode.next
        return curNode

    def getLength(self, head):
        curNode = head
        count = 0
        while (curNode is not None):
            count += 1
            curNode = curNode.next
        return count
