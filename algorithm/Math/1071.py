'''
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/

For strings S and T, we say "T divides S" if and only if 
S = T + ... + T  (T concatenated with itself 1 or more times)
Return the largest string X such that X divides str1 and X divides str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
'''
from typing import *

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1:
            return str2
        if not str2:
            return str1
        if str1==str2:
            return str1
        if len(str2)>len(str1):
            str1,str2=str2,str1
        if str1[:len(str2)]!=str2:
            return ""
        # return GCD(b, a%b)
        return self.gcdOfStrings(str2, str1[len(str2):])

print(Solution().gcdOfStrings("ABCABC","ABC"))
#ABC
print(Solution().gcdOfStrings("ABABAB","ABAB"))
#AB
print(Solution().gcdOfStrings("LEET","CODE"))
#""