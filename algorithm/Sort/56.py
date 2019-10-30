'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, 
merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, 
merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
from typing import *

#Concise
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda inter: inter[0])
        ans = [intervals[0]]
        for idx in range(1, len(intervals)):
            startI, endI = intervals[idx]
            if startI <= ans[-1][1]:
                ans[-1][1] = max(endI, ans[-1][1])
            else:
                ans.append(intervals[idx])
        return ans

#Ugly
class UglySolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda inter: inter[0])
        latestEnd = intervals[0][1]
        ans = [intervals[0]]
        for idx in range(1, len(intervals)):
            startI, endI = intervals[idx]
            if startI <= latestEnd:
                latestEnd = max(endI, ans[-1][1])
                ans[-1][1] = latestEnd
            else:
                ans.append(intervals[idx])
                latestEnd = endI
        return ans

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
#[[1,6],[8,10],[15,18]]
print(Solution().merge([[1,4],[4,5]]))
#[[1,5]]
print(Solution().merge([[1,4],[2,3]]))
#[[1,4]]
print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
#[[1,10]]