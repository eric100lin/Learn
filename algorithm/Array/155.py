'''
155. Min Stack
https://leetcode.com/problems/min-stack/

Hi, here's your problem today. 
This problem was recently asked by Uber:

Design a simple stack that supports 
push, pop, top, and 
retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Note: be sure that pop() and top() handle being called 
on an empty stack.
'''
from typing import *

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.minmum = []

    def push(self, x: int) -> None:
        self.values.append(x)
        newMin = x
        if self.minmum:
            # set newMin then update
            newMin = min(newMin, self.minmum[-1])
        self.minmum.append(newMin)

    def pop(self) -> None:
        if self.values:
            self.values.pop()
            self.minmum.pop()

    def top(self) -> int:
        if self.values:
            return self.values[-1]
        return None

    def getMin(self) -> int:
        if self.minmum:
            return self.minmum[-1]
        return None


import unittest
class MinStackTest(unittest.TestCase):
    def testExample(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(-3, minStack.getMin())
        minStack.pop()
        self.assertEqual(0, minStack.top())
        self.assertEqual(-2, minStack.getMin())
    def testEmptyCase(self):
        minStack = MinStack()
        minStack.pop()
        self.assertEqual(None, minStack.top())
        self.assertEqual(None, minStack.getMin())
    def testEdgeCase(self):
        minStack = MinStack()
        minStack.push(1)
        self.assertEqual(1, minStack.getMin())
        self.assertEqual(1, minStack.top())
        minStack.pop()
        self.assertEqual(None, minStack.top())
        self.assertEqual(None, minStack.getMin())

if __name__ == "__main__":
    unittest.main()