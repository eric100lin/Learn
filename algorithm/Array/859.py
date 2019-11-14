'''
859. Buddy Strings
https://leetcode.com/problems/buddy-strings/

Hi, here's your problem today. This problem was recently asked by AirBNB:

Given two strings A and B of lowercase letters, return true if and only if 
we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false
'''
from typing import *
import collections

class Solution:
    def buddyStrings(self, A, B):
        # NG Case 1: length not equal
        # NG Case 2: either of them is empty
        if len(A)!=len(B) or len(A)==0 or len(B)==0:
            return False
        diff = []
        dict = collections.defaultdict(int)
        for i in range(len(A)):
            dict[A[i]] += 1
            if A[i]!=B[i]:
                diff.append(i)
        # OK Case 1: no different with duplicate letters
        if not diff:
            for count in dict.values():
                if count>=2:
                    return True
        # OK Case 2: just two differents and match after exchange
        elif len(diff)==2:
            if A[diff[0]] == B[diff[1]] and \
               A[diff[1]] == B[diff[0]]:
               return True
        return False

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False