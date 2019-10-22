'''
15. 3Sum
https://leetcode.com/problems/3sum/

Given an array nums of n integers, 
are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sorted take nlogn here since brute foce take n*n*n
        nums = sorted(nums)
        
        # NG Case: Length OK(>= 3) but all zeros
        if (len(nums) >= 3) and (nums[0] == nums[len(nums) -1]) and (nums[0] == 0):
            return [[0, 0, 0]]
        
        triplets = []
        # 0~lenght-2, two for left and right pointers
        for index in range(len(nums) - 2):
            left = index + 1
            right = len(nums) - 1
            # two pointers sinces sorted
            while left < right:
                sum = nums[index] + nums[left] + nums[right]
                if sum == 0:
                    #Use tuple here, since 'list' is unhashable!!
                    triplets.append((nums[index],nums[left],nums[right]))
                    left += 1
                    right -= 1
                elif sum < 0:
                    # Move left+1 to sum larger
                    left += 1
                else:
                    # Move right-1 to sum smaller
                    right -= 1
        # Use set to filter out duplicate
        # All duplicates are same elements since sorted
        return list(set(triplets))

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
#[  [-1, 0, 1],[-1, -1, 2] ]
print(Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
#[[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
