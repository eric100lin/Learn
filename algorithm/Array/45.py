'''
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers, 
you are initially positioned at the first index of the array.
Each element in the array represents 
your maximum jump length at that position.
Your goal is to reach the last index 
in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: 
The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
from typing import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return 0

        cnt = till = 0
        maxIdx = 0
        for i in range(N):
            maxIdx = max(maxIdx, i + nums[i])
            if i == till:
                cnt += 1
                till = maxIdx

            if till >= N - 1:
                break
        return cnt

print(Solution().jump([2,3,0,0,4]))
