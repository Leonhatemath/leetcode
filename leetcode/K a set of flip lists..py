# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        current_node = head
        count = 0
        while current_node and count < k:
            current_node = current_node.next
            count += 1
        if count == k:
            current_node = self.reverseKGroup(current_node,k)
            while count > 0:
                tempory_node = head.next
                head.next = current_node
                current_node = head
                head = tempory_node
                count -= 1
            head = current_node
        return head
