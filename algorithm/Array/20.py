'''
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true

Hi, here's your problem today. 
This problem was recently asked by Uber:
Imagine you are building a compiler. 
Before running any code, 
the compiler must check that the parentheses 
in the program are balanced. 
Every opening bracket must have a corresponding closing bracket. 
We can approximate this using strings. 
Given a string containing just 
the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid. 
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
'''
from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Use hash map to achieve O(1) look up and
        # keeps the code very clean.
        mapping = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in mapping:
                if not stack or stack[-1]!=mapping[ch]:
                    return False
                stack.pop()
            else:
                # containing just valid characters
                stack.append(ch)
        return not stack

import unittest

class ValidParenthesesTest(unittest.TestCase):

    def testBaseCase(self):
        self.assertEqual(Solution().isValid("()"), True)
        self.assertEqual(Solution().isValid("[]"), True)
        self.assertEqual(Solution().isValid("{}"), True)
    def testCombination(self):
        self.assertEqual(Solution().isValid("()[]{}"), True)
        self.assertEqual(Solution().isValid("{[]}"), True)
        self.assertEqual(Solution().isValid("([{}])()"), True)
    def testInvalidCase(self):
        self.assertEqual(Solution().isValid("(]"), False)
        self.assertEqual(Solution().isValid("([)]"), False)
        self.assertEqual(Solution().isValid("()(){(())"), False)
    def testEdgeCase(self):
        self.assertEqual(Solution().isValid(""), True)
        self.assertEqual(Solution().isValid("(((((((((("), False)
        self.assertEqual(Solution().isValid("))))))))))"), False)

if __name__ == "__main__":
    unittest.main()