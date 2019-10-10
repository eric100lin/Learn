'''
38. Count and Say
https://leetcode.com/problems/count-and-say/

Hi, here's your problem today. This problem was recently asked by Google:

A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is obtained by describing the previous term. An example is easier to understand:

Each consecutive value describes the prior value.

1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # one 1, one 2, and two 1's.

Your task is, return the nth term of this sequence.
'''
from typing import *

class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        res = "1"
        for i in range(1, n):
            tmp = ""
            si = 0
            while si < len(res):
                cnt = 1
                while si+cnt < len(res) and res[si]==res[si+cnt]:
                    cnt+=1
                tmp += "{}{}".format(cnt, res[si])
                si += cnt
            res = tmp
        return res

for i in range(8):
    print(Solution().countAndSay(i))