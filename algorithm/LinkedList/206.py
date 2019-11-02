'''
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. 
Could you implement both?

Hi, here's your problem today. 
This problem was recently asked by Google:
Given a singly-linked list, reverse the list. 
This can be done iteratively or recursively. 
Can you get both solutions?
'''
from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        current_node = self
        result = []
        while current_node:
          result.append(current_node.val)
          current_node = current_node.next
        return str(result)

# Recursion
class RecursionSolution:
    def reverseList(self, head: ListNode) -> ListNode:
        # No need to check head in second or condition
        #if not head or (head and not head.next):
        if not head or not head.next:
            return head
        root = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return root

#Iteration from Recursion idea: O(n) space
class IterNSolution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        last = head
        while last and last.next:
            stack.append(last)
            last = last.next
        tmp = last
        while stack:
            tmp.next = stack[-1]
            tmp = stack.pop()
            tmp.next = None
        return last

#Iteration elegant approach: O(1) space
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            orgCurrNext = curr.next
            # Before: prev->curr->orgCurrNext
            # After:  prev<-curr  orgCurrNext
            curr.next = prev
            prev = curr
            curr = orgCurrNext
        # OK for "not head" case
        return prev

import unittest

class ReverseLinkedListTest(unittest.TestCase):

    def testExample1(self):
        #Input: 1->2->3->4->5->NULL
        root = ListNode(1)
        root.next = ListNode(2)
        root.next.next = ListNode(3)
        root.next.next.next = ListNode(4)
        root.next.next.next.next = ListNode(5)
        #Output: 5->4->3->2->1->NULL
        self.assertEqual(str(Solution().reverseList(root)), "[5, 4, 3, 2, 1]")

    def testExample2(self):
        #Input: 4->3->2->1->0-> NULL
        root = ListNode(4)
        root.next = ListNode(3)
        root.next.next = ListNode(2)
        root.next.next.next = ListNode(1)
        root.next.next.next.next = ListNode(0)
        #Output: 0->1->2->3->4->NULL
        self.assertEqual(str(Solution().reverseList(root)), "[0, 1, 2, 3, 4]")

    def testEdgeCase(self):
        self.assertEqual(str(Solution().reverseList(None)), "None")
        root = ListNode(666)
        self.assertEqual(str(Solution().reverseList(root)), "[666]")

if __name__ == "__main__":
    unittest.main()