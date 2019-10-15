'''
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/

Given an array of integers and an integer k, 
find out whether there are two distinct indices i and j in the array 
such that nums[i] = nums[j] and the absolute difference between i and j is 
at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''
from typing import *

# Elegant and concise solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for idx, num in enumerate(nums):
            if num in dict:
                if idx - dict[num] <= k:
                    return True
            dict[num] = idx
        return False

class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        # tricky! k may larger than len(nums)
        # exceed the maximum to prevent empty array, zero k...
        minDis = max(len(nums), k) + 1
        for idx in range(len(nums)):
            num = nums[idx]
            if num in dict:
                distance = idx - dict[num]
                minDis = min(minDis, distance)
            dict[num] = idx
        return minDis <= k

print(Solution().containsNearbyDuplicate([1,2,3,1], 3))
# True
print(Solution().containsNearbyDuplicate([1,0,1,1], 1))
# True
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))
# False
print(Solution().containsNearbyDuplicate([1,2,3,4,5,6,7,8,9,10], 15))
# False
print(Solution().containsNearbyDuplicate([], 0))
# False