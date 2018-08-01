# Slower than 100% of all solutions woohoo!!!

class LinkedList():
    def __init__(self, head):
        self.head = head


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None:
            return head
        myList = LinkedList(head)

        size = 0
        cur = myList.head
        while cur:
            cur = cur.next
            size += 1

        k %= size

        for x in range(k):
            cur = myList.head
            while cur.next.next is not None:
                cur = cur.next
            nxt = cur.next
            cur.next = None
            nxt.next = myList.head
            myList.head = nxt
        return myList.head
