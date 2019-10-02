'''
75. Sort Colors
https://leetcode.com/problems/sort-colors/

Hi, here's your problem today. This problem was recently asked by Apple:

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library’s sort function for this problem.

Can you do this in a single pass?

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #R(0) W(1) B(2)
        R = 0
        B = len(nums)-1
        i = 0
        while i<= B:
            #R(0)
            if nums[i] == 0:
                nums[i],nums[R] = nums[R],nums[i]
                R += 1
                i += 1
            #B(2)
            elif nums[i] == 2:
                nums[i],nums[B] = nums[B],nums[i]
                B -= 1
            else:
                i += 1

nums = [2,0,2,1,1,0]
Solution().buildTree(nums)
print(nums)