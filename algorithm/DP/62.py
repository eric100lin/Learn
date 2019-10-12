'''
62. Unique Paths
https://leetcode.com/problems/unique-paths/

Hi, here's your problem today. This problem was recently asked by Microsoft:

You 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.

1 1 1
1 2 3
1 3 6
'''
from typing import *

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==0 or n==0:
            return 0
        
        dp = [[0]*n for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1        #Can only move right
        for j in range(m):
            dp[j][0] = 1        #Can only move down
        
        #Start from 1,1 since this is the first cell 
        #have both direction and avoid m,n=(1,1) case!!
        for j in range(1, m):
            for i in range(1, n):
                up = dp[j-1][i]
                left = dp[j][i-1]
                dp[j][i] = up + left
        
        return dp[-1][-1]

print(Solution().uniquePaths(2, 2))
# 2
print(Solution().uniquePaths(3, 3))
# 6
print(Solution().uniquePaths(3, 2))
# 3
print(Solution().uniquePaths(1, 1))
# 1
print(Solution().uniquePaths(0, 0))
# 0