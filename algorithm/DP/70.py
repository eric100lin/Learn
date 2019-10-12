'''
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

Hi, here's your problem today. This problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.
'''
from typing import *

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0] * (n+1) #Skip dp[0]!!
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1): #Start from 3!!
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

import math

def c(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

def staircase(n):
    ways = 1
    posibleTwoSteps = n//2
    for t in range(1, posibleTwoSteps+1):
        ways += c(n-t, t)
    return ways

print(Solution().climbStairs(2))
print(staircase(2))
# 2
print(Solution().climbStairs(3))
print(staircase(3))
# 3
print(Solution().climbStairs(4))
print(staircase(4))
# 5
print(Solution().climbStairs(5))
print(staircase(5))
# 8
#1,1,1,1,1
#1,1,1,2 C(4,1)=4!/1!*(4-1)!=24/1*6=4
#1,1,2,1
#1,2,1,1
#2,1,1,1
#1,2,2 C(3,2)=3!/2!*(3-2)!=6/2=3
#2,1,2
#2,2,1

#5//2=2

print(Solution().climbStairs(10))
print(staircase(10))
