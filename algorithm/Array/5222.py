'''
5222. Split a String in Balanced Strings
https://leetcode.com/contest/weekly-contest-158/problems/split-a-string-in-balanced-strings/

Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", 
each substring contains same number of 'L' and 'R'.

Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", 
each substring contains same number of 'L' and 'R'.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Constraints:
1 <= s.length <= 1000
s[i] = 'L' or 'R'
'''
from typing import *

class Solution:
    #Easy and Good solution
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        blance = 0
        for ch in s:
            if ch == 'L':
                blance += 1
            elif ch == 'R':
                blance -= 1
            if blance == 0:
                ans += 1
        return ans

    #Complicated solution
    #https://leetcode.com/problems/split-a-string-in-balanced-strings/discuss/403793/Python-dictionary-solution
    def balancedStringSplitX(self, s: str) -> int:
        ans = 0
        dict = collections.defaultdict(int)
        for ch in s:
            dict[ch] += 1
            if dict['L']==dict['R']:
                ans += 1
                dict['L'] = dict['R'] = 0
        return ans

print(Solution().balancedStringSplit("RLRRLLRLRL"))
#4
print(Solution().balancedStringSplit("RLLLLRRRLR"))
#3
print(Solution().balancedStringSplit("LLLLRRRR"))
#1
