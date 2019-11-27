'''
1262. Greatest Sum Divisible by Three
https://leetcode.com/contest/weekly-contest-163/problems/greatest-sum-divisible-by-three/

Given an array nums of integers, 
we need to find the maximum possible sum of elements 
of the array such that it is divisible by three.

Example 1:
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: 
Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

Example 2:
Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.

Example 3:
Input: nums = [1,2,3,4,4]
Output: 12
Explanation: 
Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).

Constraints:
1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
'''
from typing import *

import heapq
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        totalSum = 0
        mod1Heap, mod2Heap = [], []
        for num in nums:
            mod = num % 3
            totalSum += num 
            if mod == 1:
                heapq.heappush(mod1Heap, num)
            elif mod == 2:
                heapq.heappush(mod2Heap, num)
        # Divide the whole list into three parts: mod_0, mod_1, mod_2.
        # Think about the sum of the original list, 
        # if it mods 3 == 0, then we can just return the sum.
        # If tot_sum % 3 == 1, then we should remove 
        # one smallest element from mod_1 or two smallest ones from mod_2.
        # If tot_sum % 3 == 2, then we should remove 
        # one smallest element from mod_2 or two smallest ones from mod_1.
        if totalSum % 3 == 0:
            remove = 0
        elif totalSum % 3 == 1:
            remove = totalSum
            if mod1Heap:
                remove = heapq.heappop(mod1Heap)
            if len(mod2Heap) >= 2:
                remove = min(remove, heapq.heappop(mod2Heap) + heapq.heappop(mod2Heap))
        elif totalSum % 3 == 2:
            remove = totalSum
            if len(mod1Heap) >= 2:
                remove = heapq.heappop(mod1Heap) + heapq.heappop(mod1Heap)
            if mod2Heap:
                remove = min(remove, heapq.heappop(mod2Heap))
        return totalSum - remove

print(Solution().maxSumDivThree([3,6,5,1,8]))
# 18
print(Solution().maxSumDivThree([4]))
# 0
print(Solution().maxSumDivThree([1,2,3,4,4]))
# 12