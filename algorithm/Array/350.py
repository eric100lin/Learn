'''
350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
'''
from typing import *
import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dict1 = collections.defaultdict(int)
        for n in nums1:
            dict1[n] += 1
        for n in nums2:
            if n in dict1 and dict1[n]!=0:
                dict1[n] -= 1
                res.append(n)
        return res

print(Solution().intersect([1,2,2,1], [2,2]))
#[2,2]

print(Solution().intersect([4,9,5], [9,4,9,8,4]))
#[9,4]