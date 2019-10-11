'''
1. Two Sum
https://leetcode.com/problems/two-sum/

Hi, here's your problem today. This problem was recently asked by Facebook:

You are given a list of numbers, and a target number k. 
Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5, 
return true since 4 + 1 = 5.
'''
from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        complements = {}
        for i in range(len(nums)):
            number = nums[i]
            if number in complements:
                ans.append(complements[number])
                ans.append(i)
            else:
                complement = target-number
                complements[complement] = i
        return ans

def two_sum(list, k):
    complements = set()
    for number in list:
        if number in complements:
            return True
        complements.add(k-number)
    return False

import unittest

class TestTwoSumLeetCodeSolution(unittest.TestCase):

    def testExampleCase1(self):
        self.assertEqual([0, 1], Solution().twoSum([2, 7, 11, 15], 9))

    def testExampleCase2(self):
        self.assertEqual([0, 2], Solution().twoSum([4,7,1,-3,2], 5))

    def testEmptyCase(self):
        self.assertEqual([], Solution().twoSum([], 5))

    def testNotFoundCase(self):
        self.assertEqual([], Solution().twoSum([1,2,6,7,9,11,19999,-3,-5], 5))

class TestTwoSum(unittest.TestCase):
    
    def testExampleCase(self):
        self.assertEqual(True, two_sum([4,7,1,-3,2], 5))

    def testEmptyCase(self):
        self.assertEqual(False, two_sum([], 5))

    def testNotFoundCase(self):
        self.assertEqual(False, two_sum([1,2,6,7,9,11,19999,-3,-5], 5))

if __name__ == "__main__":
    unittest.main()
