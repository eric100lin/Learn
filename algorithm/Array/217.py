'''
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, 
find if the array contains any duplicates.
Your function should return true if 
any value appears at least twice in the array, 
and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
from typing import *

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

print(Solution().containsDuplicate([1,2,3,1]))
#True
print(Solution().containsDuplicate([1,2,3,4]))
#False
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
#True
