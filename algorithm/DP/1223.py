'''
1223. Dice Roll Simulation
https://leetcode.com/contest/weekly-contest-158/problems/dice-roll-simulation/

A die simulator generates a random number from 1 to 6 for each roll. 
You introduced a constraint to the generator such that it cannot roll the number i 
more than rollMax[i] (1-indexed) consecutive times. 
Given an array of integers rollMax and an integer n, return 
the number of distinct sequences that can be obtained with exact n rolls.
Two sequences are considered different if at least one element differs from each other. 
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, 
there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, 
the numbers 1 and 2 appear at most once consecutively, 
therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.

Example 2:
Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30

Example 3:
Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181

Constraints:
1 <= n <= 5000
rollMax.length == 6
1 <= rollMax[i] <= 15
'''
from typing import *

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        modulo = 10 ** 9 + 7

        # dp[roll][num] represents the number of distinct sequences that
        # can be obtained when rolling 'roll' times and ending with 'num'
        dp = [[0]*7 for _ in range(n)]
        
        # First Row: 1 1 1 1 1 1 6
        for i in range(6):
            dp[0][i] = 1
        dp[0][-1] = 6
        
        for roll in range(1, n):
            sum = 0
            for num in range(6):
                # Set current row as the sum of last row
                dp[roll][num] = dp[roll - 1][-1]
                
                exceedNumRoll = roll - rollMax[num]
                if exceedNumRoll < 0:
                    # Not exceed
                    sum += dp[roll][num]
                else:
                    # Exceed
                    if exceedNumRoll - 1 >= 0:
                        # For axx1, we need to remove the number of a11 (211 + 311 + 411 + 511 + 611)
                        dp[roll][num] -= dp[exceedNumRoll-1][-1] - dp[exceedNumRoll-1][num]
                    else:
                        # For xx1, only 111 is not allowed,
                        # so we only need to remove 1 sequence from previous sum
                        dp[roll][num] -= 1
                    sum += dp[roll][num]
            dp[roll][-1] = sum % modulo
        return dp[-1][-1]

print(Solution().dieSimulator(2, [1,1,2,2,2,3]))
#34
print(Solution().dieSimulator(2, [1,1,1,1,1,1]))
#30
print(Solution().dieSimulator(3, [1,1,1,2,2,3]))
#181
print(Solution().dieSimulator(15, [1,1,1,2,2,3]))
#847568987