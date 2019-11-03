'''
1247. Minimum Swaps to Make Strings Equal
https://leetcode.com/contest/weekly-contest-161/problems/minimum-swaps-to-make-strings-equal/

You are given two strings s1 and s2 of equal length
consisting of letters "x" and "y" only.
Your task is to make these two strings equal to each other.
You can swap any two characters that belong to different strings,
which means: swap s1[i] and s2[j].
Return the minimum number of swaps required to make s1 and s2 equal,
or return -1 if it is impossible to do so.

Example 1:
Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation:
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

Example 2:
Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation:
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx",
cause we can only swap chars in different strings.

Example 3:
Input: s1 = "xx", s2 = "xy"
Output: -1

Example 4:
Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4

Constraints:
1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.
'''
from typing import *

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0

        for c1, c2 in zip(s1, s2):
            if c1=='x' and c2=='y':
                xy += 1
            elif c1=='y' and c2=='x':
                yx += 1

        # if number of 'x' or 'y' is odd, we can not make s1 equals to s2
        if (xy + yx) % 2 != 0:
            return -1
        
        # Cases to do 1 swap:
        # "xx" => xy // 2 => how many pairs of 'x' we have ?
        # "yy" => yx // 2 => how many pairs of 'y' we have ?
        # 
        # Cases to do 2 swaps:
        # "xy" or "yx" =>  xy % 2
        return xy // 2 + yx // 2 + (xy % 2) * 2

import unittest

class MinSwapTest(unittest.TestCase):

    def testCase1Swap(self):
        self.assertEqual(Solution().minimumSwap(s1 = "xx", s2 = "yy"), 1)
        # s1=xx
        # s2=yy
        #    ↓↓ 0↑(yx) 2↓(xy)
        #1
        self.assertEqual(Solution().minimumSwap(s1="yy", s2="xx"), 1)
        # s1=yy
        # s2=xx
        #    ↑↑ 2↑(yx) 0↓(xy)
        #1
        self.assertEqual(Solution().minimumSwap(s1="xxxx", s2="yyyy"), 2)
        # s1=xxxx
        # s2=yyyy
        #    ↓↓↓↓ 0↑(yx) 4↓(xy)
        # 2

    def testCase2Swap(self):
        self.assertEqual(Solution().minimumSwap(s1 = "xy", s2 = "yx"), 2)
        # s1=xy
        # s2=yx
        #    ↓↑ 1↑(yx) 1↓(xy)
        #2

    def testMixedCase(self):
        self.assertEqual(Solution().minimumSwap(s1 = "xyxx", s2 = "yxyy"), 3)
        # s1=xyxx
        # s2=yxyy
        #    ↓↑↓↓ 1↑(yx) 3↓(xy)
        #3
        self.assertEqual(Solution().minimumSwap(s1 = "xxyxy", s2 = "yyyyx"), 3)
        # s1=xxyxy
        # s2=yyyyx
        #    ↓↓ ↓↑ 1↑(yx) 3↓(xy)
        # 3
        self.assertEqual(Solution().minimumSwap(s1="xxyyxyxyxx", s2="xyyxyxxxyx"), 4)
        # s1=xxyyxyxyxx
        # s2=xyyxyxxxyx
        #     ↓ ↑↓↑ ↑↓  3↑(yx) 3↓(xy)
        # 4

    def testInvalidCase(self):
        self.assertEqual(Solution().minimumSwap(s1="xx", s2="xy"), -1)
        # s1=xx
        # s2=xy
        #     ↓ 0↑(yx) 1↓(xy)
        #-1
        self.assertEqual(Solution().minimumSwap(s1 = "xyxx", s2 = "yyyy"), -1)
        # s1=xyxx
        # s2=yyyy
        #    ↓ ↓↓ 0↑(yx) 3↓(xy)
        #-1

if __name__ == "__main__":
    unittest.main()

#2,2,2,1,2,2,1
#2,2,2,1,2,2,1,2
#2,2,2,1,2,2,1,2,2
#2,2,2,1,2,2,1,2,2,2
#  2,2,1,2,2,1,2,2,2
#    2,1,2,2,1,2,2,2
#      1,2,2,1,2,2,2
#      1,2,2,1,2,2
#      1,2,2,1,2
#      1,2,2,1
#    2,1,2,2,1
#    2,1,2,2,1,2
#    2,1,2,2,1,2,2
#  2,2,1,2,2,1
#  2,2,1,2,2,1,2
#  2,2,1,2,2,1,2,2