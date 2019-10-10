'''
228. Summary Ranges
https://leetcode.com/problems/summary-ranges/

Hi, here's your problem today. This problem was recently asked by Facebook:

Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

Example:
Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
Output: ['0->2', '5', '7->11', '15->15']
Assume that all numbers will be greater than or equal to 0, and each element can repeat.

'''
from typing import *

#Ugly
def findRanges(nums):
    result = []
    start = 0
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1] and nums[i]!=nums[i-1]+1:
            if start==i-1:
                result.append("{}".format(nums[start]))
            else:
                result.append("{}->{}".format(nums[start], nums[i-1]))
            start = i
    if nums:
        if start==len(nums)-1:
            result.append("{}".format(nums[start]))
        else:
            result.append("{}->{}".format(nums[start], nums[-1]))
    return result

#Good
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start,n = 0, len(nums)
        while start < n:
            end = start+1
            while end<n and \
                (nums[end]==nums[end-1] or \
                 nums[end]==nums[end-1]+1):
                end += 1
            if start==(end-1):
                result.append("{}".format(nums[start]))
            else:
                result.append("{}->{}".format(nums[start], nums[end-1]))
            start = end
        return result

print(Solution().summaryRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5', '7->11', '15->15']