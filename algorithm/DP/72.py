'''
72. Edit Distance
https://leetcode.com/problems/edit-distance/

Hi, here's your problem today. This problem was recently asked by AirBNB:

Given two strings, determine the edit distance between them. 
The edit distance is defined as the minimum number of edits 
(insertion, deletion, or substitution) needed to change one string to the other.

For example, "biting" and "sitting" have an 
edit distance of 2 (substitute b for s, and insert a t).
'''
from typing import *

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #   b, i, t, i, n, g
        # s 2,←2, 3, 4, 5, 6, 7
        #   ↑ ↖                
        # i 2, 1, 2, 3, 4, 5, 6
        #       ↖             
        # t 2, 1, 1,←2, 3, 4, 5
        #         ↑ ↖          
        # t 2, 1, 0, 1, 2, 3, 4
        #          ↖          
        # i 3, 2, 1, 0, 1, 2, 3
        #             ↖       
        # n 4, 3, 2, 1, 0, 1, 2
        #                ↖    
        # g 5, 4, 3, 2, 1, 0, 1
        #                   ↖ 
        #   6, 5, 4, 3, 2, 1, 0
        
        dp = [[0]*(1+len(word1)) for _ in range(1+len(word2))]
        for j in range(len(word2), -1, -1):
            for i in range(len(word1), -1, -1):
                if i == len(word1):
                    dp[j][i] = len(word2)-j
                elif j == len(word2):
                    dp[j][i] = len(word1)-i
                elif word1[i] == word2[j]:
                    dp[j][i] = dp[j+1][i+1]
                else:
                    dp[j][i] = 1 + min(dp[j+1][i], dp[j][i+1], dp[j+1][i+1])
        return dp[0][0]

print(Solution().minDistance('biting', 'sitting'))
# 2
