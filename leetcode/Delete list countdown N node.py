# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def CreatNode(nums):
    for i in range(len(nums)-1):
        head_node = 


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_list = []
        head_node = head
        while node_list[-1].next != None:
            node_list.append(head)
            if len(node_list) > n + 1:
                node_list.pop(0)
            head = head.next
        node_list[0].next = node_list[2]
        node_list[1].next = None
        return head_node