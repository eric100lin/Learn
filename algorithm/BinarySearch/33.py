'''
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at
some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search.
If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[left]:
                # left half sorted, target in sorted part
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid+1
            else:
                # right half sorted, target in sorted part
                if nums[mid] < target <= nums[right-1]:
                    left = mid+1
                else:
                    right = mid
        return -1

print(Solution().search(nums = [4,5,6,7,0,1,2], target = 0))
#4
print(Solution().search(nums = [4,5,6,7,0,1,2], target = 3))
#-1
print(Solution().search(nums = [4,5,6,7,0,1,2], target = 2))
#6