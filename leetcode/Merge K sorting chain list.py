# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head_nodes = [l for l in lists]
        node_val = []
        for node in head_nodes:
            if node:node_val.append(node.val)
        if node_val == []:
            return []
        head_node = ListNode(0)
        result = head_node
        while head_nodes != []:
            index = node_val.index(min(node_val))
            min_node = head_nodes[index]
            head_node.next = min_node
            if min_node.next:
                min_node = min_node.next
                head_nodes[index] = min_node
                node_val[index] = min_node.val
            else:
                del head_nodes[index]
                del node_val[index]
            head_node = head_node.next
        return result.next