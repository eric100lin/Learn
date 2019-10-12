'''
1171. Remove Zero Sum Consecutive Nodes from Linked List
https://leetcode.com/contest/weekly-contest-151/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

Given the head of a linked list, 
we repeatedly delete consecutive sequences of nodes that 
sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.
You may return any such answer.

(Note that in the examples below, 
all sequences are serializations of ListNode objects.)

Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:
Input: head = [1,2,3,-3,4]
Output: [1,2,4]

Example 3:
Input: head = [1,2,3,-3,-2]
Output: [1]

Constraints:
The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
'''
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        root = ListNode(0)
        root.next = head
        dict = {}
        dict[0] = root
        ac = 0
        while head:
            ac += head.val
            if ac in dict:
                aux_ac = ac      #It's important to have aux_ac do delete key in dict
                pre = dict[ac]
                while pre!=head:
                    pre = pre.next
                    aux_ac += pre.val
                    if pre!=head:
                        del dict[aux_ac]
                dict[ac].next = head.next   #Use dict[ac] to get the parent
            else:
                dict[ac] = head
            head = head.next
        return root.next

head = ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(-3)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(1)
r=Solution().removeZeroSumSublists(head)

tmp = r
while tmp:
    print(tmp.val,end=' ')
    tmp = tmp.next
