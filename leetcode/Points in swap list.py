# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = ListNode(0)
        node.next = head
        P1 = head
        P2 = head.next
        if P2:result = P2
        else:return head
        while P1 and P2:
            node.next = P2
            P1.next = P2.next
            P2.next = P1
            node = P1
            if node.next:
                P1 = node.next
            else:P1 = None
            if P1 and P1.next:
                P2 = P1.next
            else:P2 = None
        return result