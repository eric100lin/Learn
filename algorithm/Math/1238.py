'''
1238. Circular Permutation in Binary Representation
https://leetcode.com/contest/weekly-contest-160/problems/circular-permutation-in-binary-representation/

Given 2 integers n and start. 
Your task is return any permutation p of (0,1,2.....,2^n -1) such that :
 * p[0] = start
 * p[i] and p[i+1] differ by only one bit 
   in their binary representation.
 * p[0] and p[2^n -1] must also differ by 
   only one bit in their binary representation.

Example 1:
Input: n = 2, start = 3
Output: [3,2,0,1]
Explanation: 
The binary representation of the permutation is (11,10,00,01). 
All the adjacent element differ by one bit. 
Another valid permutation is [3,1,0,2]

Example 2:
Input: n = 3, start = 2
Output: [2,6,7,5,4,0,1,3]
Explanation: 
The binary representation of the permutation is 
(010,110,111,101,100,000,001,011).

Constraints:
1 <= n <= 16
0 <= start < 2 ^ n
'''
from typing import *

# Approach 1: reflect-and-prefix method
# https://en.wikipedia.org/wiki/Gray_code
class SolutionBad:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = []
        gray = [0,1]
        for i in range(1, n):
            reflectAdd = 2**i
            for gidx in range(len(gray)-1,-1,-1):
                gray.append(gray[gidx]+reflectAdd)
        # list NO find(), ONLY index()
        # string have index() and find()
        startidx = gray.index(start)
        for count in range(len(gray)):
            ans.append(gray[startidx])
            startidx = (startidx+1) % len(gray)
        return ans
#Gray code
#n=1 2  3
#  0 00 000
#  1 01 001
#    11 011
#    10 010
#       110
#       111
#       101
#       100

# Approach 2: x ^ (x>>1)
#n=2  = x  ^ x>>1
#  00   00    00
#  01   01    00
#  11   10    01
#  10   11    01
#n=3   =  x  ^ x>>1
#  000   000   000
#  001   001   000
#  011   010   001
#  010   011   001
#  110   100   010
#  111   101   010
#  101   110   011
#  100   111   011
#gray XOR start  ans
#  00  ^   11    11
#  01  ^   11    10
#  11  ^   11    00
#  10  ^   11    01
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ i ^ (i >> 1) for i in range(1 << n)]

print(Solution().circularPermutation(2, 3))
# [3,2,0,1]
# [3,1,0,2]
print(Solution().circularPermutation(3, 2))
print(SolutionBad().circularPermutation(3, 2))
# [2, 3, 1, 0, 4, 5, 7, 6]
# [2, 3, 1, 0, 4, 5, 7, 6]

# TMP:
# ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
# https://docs.python.org/3/library/collections.html#collections.Counter