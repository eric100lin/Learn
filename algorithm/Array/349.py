'''
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/

Hi, here's your problem today. This problem was recently asked by Amazon:

Given two arrays, write a function to compute their intersection - 
the intersection means the numbers that are in both arrays.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.
'''
from typing import *

class Solution:
    #Ugly
    def intersectionUgly(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        inter = set()
        for n in nums2:
            if n in set1:
                inter.add(n)
        return list(inter)
    #Good
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        # Can NOT use "and", should use "&"
        return list(set1 & set2)

print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]