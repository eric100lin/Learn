'''
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, 
we use an integer pos which represents 
the position (0-indexed) in the linked list 
where tail connects to. 
If pos is -1, 
then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: 
There is a cycle in the linked list, 
where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: 
There is a cycle in the linked list, 
where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: 
There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
'''
from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Concise
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow,fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

#Ugly
class UglySolution:
    def hasCycle(self, head: ListNode) -> bool:
        slow,quick = head,None
        if head and head.next and head.next.next:
            quick = head.next.next
        while slow and quick:
            if slow==quick:
                return True
            slow = slow.next
            quick=quick.next
            if quick:
                quick=quick.next
        return False

root = ListNode(3)
root.next = dup = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)
root.next.next.next.next = dup
print(Solution().hasCycle(root))
#True

root = dup = ListNode(1)
root.next = ListNode(2)
root.next.next = dup
print(Solution().hasCycle(root))
#True

root = ListNode(1)
print(Solution().hasCycle(root))
#False