'''
172. Factorial Trailing Zeroes
https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros

Be careful 1000! has 2568 digits...
'''
from typing import *

class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n != 0:
            zeros += n//5
            n //= 5
        return zeros

print(Solution().trailingZeroes(3))
#0
print(Solution().trailingZeroes(5))
#1
print(Solution().trailingZeroes(6))
#1
print(Solution().trailingZeroes(12))
#2
print(Solution().trailingZeroes(24))
#4
print(Solution().trailingZeroes(25))
#6
print(Solution().trailingZeroes(49))
#10
print(Solution().trailingZeroes(50))
#12
