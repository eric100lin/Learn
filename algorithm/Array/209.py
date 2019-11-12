'''
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-subSum/

Hi, here's your problem today. This problem was recently asked by Amazon:

Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the subSum ≥ s. 
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length 
under the problem constraint.
'''
from typing import *

class Solution:
    def minSubArrayLen(self, nums, s):
        subSum = 0
        left = 0
        # Use N+1 to indicate "If there isn't one, return 0 instead"
        minLength = len(nums) + 1
        for idx,num in enumerate(nums):
            subSum += num
            while subSum >= s:
                # minus with left, not effect i
                minLength = min(minLength, idx-left+1)
                subSum -= nums[left]
                left += 1
        # Important!! Edge Case!!
        # Check sum of all array elements < s here
        if minLength == len(nums) + 1:
            minLength = 0
        return minLength

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2