'''
1224. Maximum Equal Frequency
https://leetcode.com/contest/weekly-contest-158/problems/maximum-equal-frequency/

Given an array nums of positive integers,
return the longest possible length of an array prefix of nums,
such that it is possible to remove exactly one element from this prefix
so that every number that has appeared in it will have the same number of occurrences.
If after removing one element there are no remaining elements,
it's still considered that every appeared number has the same number of ocurrences (0).

Example 1:
Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7,
if we remove nums[4]=5, we will get [2,2,1,1,3,3],
so that each number will appear exactly twice.

Example 2:
Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13

Example 3:
Input: nums = [1,1,1,2,2,2]
Output: 5

Example 4:
Input: nums = [10,2,8,9,3,8,1,5,2,3,7,6]
Output: 8

Constraints:
2 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''
from typing import *
import collections

# https://leetcode.com/problems/maximum-equal-frequency/discuss/403628/Easy-Python-Solution-Concise-10-lines-Explained-O(N)
# cnt records the occurence of each num, freq records the frequence of number of occurences. maxF is the largest frequence.
# There are three cases which satify the condition:
#  1.all elements appear exact once.
#  2.all elements appear maxF times, except one appears once.
#  3.all elements appear maxF-1 times, except one appears maxF.
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        cnt,freq,maxF,res = collections.defaultdict(int), collections.defaultdict(int),0,0
        for i,num in enumerate(nums):
            cnt[num] += 1
            freq[cnt[num]-1] -= 1
            freq[cnt[num]] += 1
            maxF = max(maxF,cnt[num])
            if maxF*freq[maxF] == i or (maxF-1)*(freq[maxF-1]+1) == i or maxF == 1:
                res = i + 1
        return res

print(Solution().maxEqualFreq([2,2,1,1,5,3,3,5]))
#7
print(Solution().maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5]))
#13
print(Solution().maxEqualFreq([1,1,1,2,2,2]))
#5
print(Solution().maxEqualFreq([10,2,8,9,3,8,1,5,2,3,7,6]))
#8