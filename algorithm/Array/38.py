'''
38. Count and Say
https://leetcode.com/problems/count-and-say/

Hi, here's your problem today. 
This problem was recently asked by Google:

A look-and-say sequence is defined as 
the integer sequence beginning with a sIdxngle digit 
in which the next term is obtained by 
describing the previous term. 
An example is easIdxer to understand:

Each consecutive value describes the prior value.
1.1
2.11     # one 1's
3.21     # two 1's
4.1211   # one 2, and one 1.
5.111221 # one 1, one 2, and two 1's.

Given an integer n where 1 ≤ n ≤ 30, 
generate the nth term of the count-and-say sequence.
'''
from typing import *

class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1, n):
            tmp = ""
            sIdx = 0
            while sIdx < len(res):
                cnt = 1
                while sIdx+cnt < len(res) and res[sIdx]==res[sIdx+cnt]:
                    cnt += 1
                tmp += "{}{}".format(cnt, res[sIdx])
                sIdx += cnt
            res = tmp
        return res

for i in range(8):
    print(Solution().countAndSay(i))