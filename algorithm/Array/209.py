'''
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Hi, here's your problem today. This problem was recently asked by Amazon:

Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''
from typing import *

class Solution:
    def minSubArrayLen(self, nums, s):
        sum = 0
        left = 0
        #Use N+1 to indicate "If there isn't one, return 0 instead"
        ans = len(nums) + 1
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                #minus with left, not effect i
                ans = min(ans, i+1-left)
                sum -= nums[left]
                left += 1
        if ans == len(nums) + 1: #Check N+1 here
            ans = 0
        return ans

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2