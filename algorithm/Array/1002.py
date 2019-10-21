'''
1002. Find Common Characters
https://leetcode.com/problems/find-common-characters/

Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings 
within the list (including duplicates).
For example, if a character occurs 3 times in all strings but 
not 4 times, you need to include that 
character three times in the final answer.
You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
'''
from typing import *
import collections

class Solution:
    #Bad
    def commonCharsBad(self, A: List[str]) -> List[str]:
        if len(A)<2:
            return []
        res = []
        dicts = []
        for s in A:
            dict = collections.defaultdict(int)
            for c in s:
                dict[c] += 1
            dicts.append(dict)
        inter = set(dicts[0].keys())
        for i in range(1,len(dicts)):
            inter &= set(dicts[i].keys())
        for c in inter:
            minCnt = dicts[0][c]
            for i in range(1,len(dicts)):
                minCnt = min(minCnt, dicts[i][c])
            for i in range(minCnt):
                res.append(c)
        return res
    #Good
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A)<2:
            return []
        res = collections.Counter(A[0])
        for idx in range(1, len(A)):
            res &= collections.Counter(A[idx])
        return list(res.elements())

print(Solution().commonChars(["bella","label","roller"]))
#['e', 'l', 'l']
print(Solution().commonChars(["cool","lock","cook"]))
#['c', 'o']