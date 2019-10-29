'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums,
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.
'''
from typing import *

class DPSolution:

    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSum = nums[0]
        subSum = nums[0]
        for i in range(1, len(nums)):
            thisNum = nums[i]
            if subSum + thisNum > thisNum:
                subSum += thisNum
            else:
                subSum = thisNum
            maxSum = max(maxSum, subSum)
        return maxSum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))