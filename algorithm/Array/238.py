'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Hi, here's your problem today. This problem was recently asked by Amazon:

You are given an array of integers. Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.

For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

You cannot use division in this problem.
'''
from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        R = 1
        for i in range(1, len(nums)):
            result[i] = result[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            result[i] *= R
            R *= nums[i]
        return result

print(Solution().productExceptSelf([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]