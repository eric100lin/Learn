'''
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums,
find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
from typing import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = maxProd = nums[0]
        #print("maxProd:{0}".format(maxProd))
        for i in range(1, len(nums)):
            mulMax = curMax * nums[i]
            mulMin = curMin * nums[i]
            # keep track of a minimum current product,
            # because a large negative value could be
            # changed into positive
            curMin = min(mulMax, mulMin, nums[i])
            curMax = max(mulMax, mulMin, nums[i])
            maxProd = max(maxProd, curMax)
            #print("maxProd:{0} {1}".format(maxProd, [mulMax, mulMin, nums[i]]))
        return maxProd

print(Solution().maxProduct([-10,-2,0,-1,-2,5]))