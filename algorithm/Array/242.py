'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, 
write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
from typing import *
import collections

# Anagrams have same counters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        return sc == tc

# Anagrams have same sorted chars
class SortSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)

print(Solution().isAnagram(s = "anagram", t = "nagaram"))
# True
print(Solution().isAnagram(s = "rat", t = "car"))
# False