'''
220. Contains Duplicate III
https://leetcode.com/problems/contains-duplicate-iii/

Given an array of integers, 
find out whether there are two distinct indices i and j in the array such that 
the absolute difference between nums[i] and nums[j] is at most t and 
the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

Time complexity O(n logk)
This will give an indication that sorting is involved for k elements.

Use already existing state to evaluate next state - 
Like, a set of k sorted numbers are only needed to be tracked. 
When we are processing the next number in array, 
then we can utilize the existing sorted state and 
it is not necessary to sort next overlapping set of k numbers again.
'''
from typing import *
import collections

class SolutionTimeExceed:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        dict = {}
        for idx, num in enumerate(nums):
            for key in dict:
                if abs(key - num) <= t and idx-dict[key] <= k:
                    return True
            dict[num] = idx
        return False

# Approach 1. O(nlogk) sliding window with balanced tree
# Python do not built in balanced tree!!

# Approach 2. O(n) sliding window with bucket solution
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for n in nums:
            # Make sure window size
            if len(window) > k:
                window.popitem(False)

            bucket = n if not t else n // t
            # At most 2t items.
            for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            window[bucket] = n

        return False

print(Solution().containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0))
# True
print(Solution().containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2))
# True
print(Solution().containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))
# False
print(Solution().containsNearbyAlmostDuplicate(nums = [1,4,7,10,13,16], k = 2, t = 2))
# t = 2 means TWO bucket
# OrderedDict([(0, 1)])
# OrderedDict([(0, 1), (2, 4)])
# OrderedDict([(2, 4), (3, 7)])
# OrderedDict([(3, 7), (5, 10)])
# OrderedDict([(5, 10), (6, 13)])
# False