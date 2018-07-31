# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        lst = [head.val]

        prevNode = head
        curNode = head.next
        while curNode:

            if curNode.val not in lst:
                lst.append(curNode.val)
            else:
                value = curNode.val
                aNode = curNode

                while aNode is not None and aNode.val == value:
                    aNode = aNode.next

                prevNode.next = aNode
            prevNode = curNode
            curNode = curNode.next
        return head