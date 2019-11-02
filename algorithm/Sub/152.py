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
    def maxSubProduct(self, nums: List[int]) -> int:
        subMax = subMin = maxSubProd = nums[0]
        #print("maxSubProd:{0}".format(maxSubProd))
        for i in range(1, len(nums)):
            mulSubMax = subMax * nums[i]
            mulSubMin = subMin * nums[i]
            # keep track of a minimum current product,
            # because a large negative value could be
            # changed into positive
            subMin = min(mulSubMax, mulSubMin, nums[i])
            subMax = max(mulSubMax, mulSubMin, nums[i])
            maxSubProd = max(maxSubProd, subMax)
            #print("maxSubProd:{0} {1}".format(maxSubProd, [mulSubMax, mulSubMin, nums[i]]))
        return maxSubProd

print(Solution().maxSubProduct([2,3,-2,4]))
#6
print(Solution().maxSubProduct([-2,0,-1]))
#0