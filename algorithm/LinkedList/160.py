'''
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Hi, here's your problem today. This problem was recently asked by Apple:

You are given two singly linked lists. The lists intersect at some node. 
Find, and return the node. Note: the lists are non-cyclical.

Example:

A = 1 -> 2 -> 3 -> 4
B = 6 -> 3 -> 4 

This should return 3 (you may assume that any nodes with the same value are the same node).
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        nodeA = headA
        nodeB = headB
        AtoB = BtoA = False
        while nodeA and nodeB and nodeA != nodeB:
            nodeA = nodeA.next
            if nodeA is None:
                if AtoB:
                    return None
                AtoB = True
                nodeA = headB
            nodeB = nodeB.next
            if nodeB is None:
                if BtoA:
                    return None
                BtoA = True
                nodeB = headA
        return nodeA if nodeA == nodeB else None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        s = ''
        c = self
        while c:
            s += str(c.val) + ' '
            c = c.next
        return s

rootA = ListNode(1)
rootA.next = ListNode(2)
rootA.next.next = ListNode(3)
rootA.next.next.next = ListNode(4)
rootB = ListNode(6)
rootB.next = rootA.next.next
print(Solution().getIntersectionNode(rootA, rootB))
# 3 4

rootA = ListNode(1)
rootA.next = ListNode(2)
rootA.next.next = ListNode(3)
rootA.next.next.next = ListNode(4)
rootB = ListNode(6)
rootB.next = ListNode(7)
rootB.next.next = ListNode(8)
print(Solution().getIntersectionNode(rootA, rootB))
# None