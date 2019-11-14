'''
1172. Dinner Plate Stacks
https://leetcode.com/contest/weekly-contest-151/problems/dinner-plate-stacks/

You have an infinite number of stacks arranged in a row and 
numbered (left to right) from 0, each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:
 * DinnerPlates(int capacity): 
   Initializes the object with the maximum capacity of the stacks.
 * void push(int val):
   pushes the given positive integer val into the 
   leftmost stack with size less than capacity.
 * int pop():
   returns the value at the top of the rightmost non-empty stack and 
   removes it from that stack, and returns -1 if all stacks are empty.
 * int popAtStack(int index): 
   returns the value at the top of the stack with the given index and 
   removes it from that stack, and returns -1 if 
   the stack with that given index is empty.

Example:

Input: 
[
 "DinnerPlates","push","push","push","push","push","popAtStack",
 "push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"
]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
Output: 
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

Explanation: 
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈ 
D.pop()            // Returns 5.  The stacks are now:      4
                                                        1  3 
                                                        ﹈ ﹈  
D.pop()            // Returns 4.  The stacks are now:   1  3 
                                                        ﹈ ﹈   
D.pop()            // Returns 3.  The stacks are now:   1 
                                                        ﹈   
D.pop()            // Returns 1.  There are no stacks.
D.pop()            // Returns -1.  There are still no stacks.
'''
from typing import *

import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stackList = []
        self.notFullHeap = []

    def push(self, val: int) -> None:
        while self.notFullHeap:
            index = heapq.heappop(self.notFullHeap)
            # It's important to check range here
            # since pop() will let the stack[index] removed
            if index < len(self.stackList):
                stack = self.stackList[index]
                stack.append(val)
                return
        if self.stackList and len(self.stackList[-1])<self.capacity:
            self.stackList[-1].append(val)
            return
        stack = [val]
        self.stackList.append(stack)

    def pop(self) -> int:
        while self.stackList and not self.stackList[-1]:
            # Remove empty stack first !!
            self.stackList.pop()
        if self.stackList:
            lastStack = self.stackList[-1]
            value = lastStack.pop()
            if not lastStack:
                # Remove empty stack !
                self.stackList.pop()
            return value
        return -1

    def popAtStack(self, index: int) -> int:
        if index < len(self.stackList):
            theStack = self.stackList[index]
            if theStack:
                value = theStack.pop()
                # Multiple heappush at same index is OK!
                # (more than one space for push)
                # Let stack[i] empty is OK for push!
                heapq.heappush(self.notFullHeap, index)
                return value
        return -1

d = DinnerPlates(2)
d.push(1)
d.push(2)
d.push(3)
d.push(4)
print(d.popAtStack(1))
print(d.popAtStack(1))
print(d.pop())
d.push(999)
print(d.pop())
print(d.pop())
print(d.pop())
print(d.pop())
