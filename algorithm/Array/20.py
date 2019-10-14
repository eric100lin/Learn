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

print(Solution().isValid("()"))
#True
print(Solution().isValid("[]"))
#True
print(Solution().isValid("{}"))
#True
print(Solution().isValid("()[]{}"))
#True
print(Solution().isValid("{[]}"))
#True

print(Solution().isValid("(]"))
#False
print(Solution().isValid("([)]"))
#False