'''
1239. Maximum Length of a Concatenated String with Unique Characters
https://leetcode.com/contest/weekly-contest-160/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

Given an array of strings arr. 
String s is a concatenation of a sub-sequence of arr which have unique characters.
Return the maximum possible length of s.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
'''
from typing import *

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Put empty set to:
        # 1.Each set(str) will put into concatSets
        # 2.Consider no unique characters case
        concatSets = [set()]
        for str in arr:
            strLength = len(str)
            strSet = set(str)
            # Check all unique: len(set) vs len(str)
            if len(strSet) != strLength:
                continue
            for cSet in concatSets:
                # Check NO intersection
                if not strSet & cSet:
                    # Put union
                    concatSets.append(strSet | cSet)
        # Get max len of sets in list
        # only empty set case considered
        return max(len(s) for s in concatSets)

print(Solution().maxLength(["cha","r","act","ers"]))