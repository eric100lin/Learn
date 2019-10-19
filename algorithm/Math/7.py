'''
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

Hi, here's your problem today. This problem was recently asked by LinkedIn:
Write a function that reverses the digits a 32-bit signed integer, x. 
Assume that the environment can only store integers within 
the 32-bit signed integer range, [-2^31, 2^31 - 1]. 
The function returns 0 when the reversed integer overflows.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−2**31,  2**31 − 1]. 
For the purpose of this problem, assume that your function returns 0 
when the reversed integer overflows.
'''
from typing import *

class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = 1 if x>0 else -1
        # Very important to turn negative value into positive value
        # or we will stuck in the while loop since
        # floor division of negative never got zero!! e.g. -1//10 is -1
        x *= sign
        while x != 0:
            ans = ans * 10 + (x % 10)
            x //= 10
        ans *= sign
        if ans > (2**31 - 1) or ans < -(2**31):
            ans = 0
        return ans

import unittest
class ReverseIntegerTest(unittest.TestCase):
    def testExample1(self):
        ans = Solution().reverse(123)
        self.assertEqual(ans, 321)
    def testExample2(self):
        ans = Solution().reverse(-123)
        self.assertEqual(ans, -321)
    def testExample3(self):
        ans = Solution().reverse(120)
        self.assertEqual(ans, 21)
    def testOverflow(self):
        ans = Solution().reverse(2**31)
        self.assertEqual(ans, 0)
        ans = Solution().reverse(-2**31-1)
        self.assertEqual(ans, 0)
    def testEdgeCase(self):
        ans = Solution().reverse(0)
        self.assertEqual(ans, 0)
        ans = Solution().reverse(-1)
        self.assertEqual(ans, -1)
        ans = Solution().reverse(9)
        self.assertEqual(ans, 9)
        ans = Solution().reverse(-9)
        self.assertEqual(ans, -9)
        ans = Solution().reverse(10)
        self.assertEqual(ans, 1)
        ans = Solution().reverse(-10)
        self.assertEqual(ans, -1)

if __name__ == "__main__":
    unittest.main()