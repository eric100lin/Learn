'''
838. Push Dominoes
https://leetcode.com/problems/push-dominoes

Hi, here's your problem today. This problem was recently asked by Twitter:

Given a string with the initial condition of dominoes, where:

. represents that the domino is standing still
L represents that the domino is falling to the left side
R represents that the domino is falling to the right side

Figure out the final position of the dominoes. 
If there are dominoes that get pushed on both ends, 
the force cancels out and that domino remains upright.

Example:
Input:  ..R...L..R.
Output: ..RR.LL..RR
'''
from typing import *

class Solution:
    #Good
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes) # Extract length as variable "N"
        force = [0]*N
        
        # Populate forces going from left to right
        f = 0
        for i in range(N):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                # Reset 'R' force if encounter 'L'!!
                f = 0
            else:
                f = max(f-1, 0) #Replace of "if f-1>=0: f-=1"
            force[i] = f
        
        # Populate forces going from right to left
        for i in range(N-1,-1,-1):
            if dominoes[i] == 'R':
                f = 0
            elif dominoes[i] == 'L':
                # Reset 'L' force if encounter 'R'!!
                f = N
            else:
                f = max(f-1, 0)
            force[i] -= f
        
        ans = ""
        for f in force:
            if f == 0:
                ans += '.'
            elif f>0:
                ans += 'R'
            else:
                ans += 'L'
        return ans
    
    #Ugly
    def pushDominoesUgly(self, dominoes: str) -> str:
        SeenR = [None] * len(dominoes)
        SeenRindex = None
        for i, c in enumerate(dominoes):
            if c=='R':
                SeenRindex = i
            SeenR[i] = SeenRindex
            if c=='L':
                SeenRindex = None
        i = len(dominoes)-1
        while i>=0:
            c = dominoes[i]
            if c=='L':
                if SeenR[i] is not None:
                    if (i-SeenR[i])%2 == 0:
                        SeenR[(i+SeenR[i])//2] = None
                    for j in range(i, (i+SeenR[i])//2, -1):
                        SeenR[j] = 'L'
                        i -= 1
                    continue
                else:
                    SeenR[i] = 'L'
                    for j in range(i-1, -1, -1):
                        if dominoes[j]=='L':
                            break
                        SeenR[j] = 'L'
                        i -= 1
            elif SeenR[i] is None:
                SeenR[i] = '.'
            else:
                SeenR[i] = 'R'
            i -= 1
        return ''.join(SeenR)

print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR
print(Solution().pushDominoes('.L.R...LR..L..'))
# LL.RR.LLRRLL..
print(Solution().pushDominoes('RR.L'))
# RR.L
print(Solution().pushDominoes('L.....RR.RL.....L.R.'))
# L.....RRRRLLLLLLL.RR