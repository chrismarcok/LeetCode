# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        lst = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next
        nodeList = []
        for x in range(len(lst) - 1, -1, -1):
            newNode = ListNode(lst[x])
            nodeList.append(newNode)
        for x in range(len(nodeList)-1):
            nodeList[x].next = nodeList[x + 1]
        return nodeList[0]