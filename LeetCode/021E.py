# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        newList = ListNode(0)
        result = newList
        curNode1, curNode2 = l1, l2

        while not (curNode1 is None and curNode2 is None):

            if curNode1 is None and curNode2.next is None:
                newList.val = curNode2.val
                curNode2 = curNode2.next

            elif curNode2 is None and curNode1.next is None:
                newList.val = curNode1.val
                curNode1 = curNode1.next
            elif curNode1 is None:
                newList.val = curNode2.val
                tempNode = ListNode(0)
                newList.next = tempNode
                newList = tempNode
                curNode2 = curNode2.next
            elif curNode2 is None:
                newList.val = curNode1.val
                tempNode = ListNode(0)
                newList.next = tempNode
                newList = tempNode
                curNode1 = curNode1.next
            elif curNode1.val < curNode2.val:
                newList.val = curNode1.val
                tempNode = ListNode(0)
                newList.next = tempNode
                newList = tempNode
                curNode1 = curNode1.next
            else:
                newList.val = curNode2.val
                tempNode = ListNode(0)
                newList.next = tempNode
                newList = tempNode
                curNode2 = curNode2.next
        return result
