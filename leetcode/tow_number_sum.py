class Listnode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def Num_to_listnode(number):
    head_node = Listnode(None)
    temper_node = Listnode(None)
    if number != 0:
        while number != 0:
            x = number % 10
            number //= 10
            if head_node == None:
                head_node = Listnode(x)
                temper_node = head_node
            else:
                head_node = Listnode(x)
                head_node.next = temper_node
                temper_node = head_node
    else:
        head_node = Listnode(0)
    return head_node


def Listnode_to_num(listnode):
    num = 0
    while listnode.val != None:
        num = num * 10 + listnode.val
        listnode = listnode.next
    return num

"""1.递归 2.数相加，再建成链表 3.新建反向的链表再相加（思路有问题，很麻烦) 4.题目输入：[2,4,3][5,6,4]输出"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def add(self, L1, L2):
        """
        len(L1) >= len(L2)
        :param self:
        :param L1:
        :param L2:
        :return:
        """
        n = 1
        while n <= len(L2):
            L1[-n].val += L2[-n].val
            if L1[-n].val >= 10:
                L1[-n].val -= 10
                if L1[-n].next.val == None:
                    node = L1[0]
                    node.val = 1
                    L1[0].next = node
                    L1.insert(0, node)
                else:
                    L1[-n - 1].val += 1
            n += 1
        return L1[-1]

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L1 = []
        L2 = []
        while l1:
            L1.insert(0,l1)
            l1 = l1.next
        while l2:
            L2.insert(0,l2)
            l2 = l2.next
        if len(L1) >= len(L2):
            return self.add(L1, L2)
        else:
            return self.add(L2, L1)

solution = Solution()
l1 = Num_to_listnode(5)
l2 = Num_to_listnode(5)
node = solution.addTwoNumbers(l1,l2)