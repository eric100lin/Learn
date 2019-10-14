'''
539. Minimum Time Difference
https://leetcode.com/problems/minimum-time-difference/

Given a list of 24-hour clock time points in "Hour:Minutes" format, 
find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1

Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
'''
from typing import *

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        MINS_IN_DAY = 24*60
        timeSeen = [False] * MINS_IN_DAY
        minDiff = MINS_IN_DAY + 1
        
        for time in timePoints:
            H, M = time.split(':')
            timeInMinutes = 60*int(H) + int(M)
            if timeSeen[timeInMinutes]:
                # Duplicate time points eg: ["00:00","00:00"]
                return 0
            timeSeen[timeInMinutes] = True
        
        # Sorted timePoints obtained! 
        firstMinutes, preMinutes = None, None
        for i in range(MINS_IN_DAY):
            if timeSeen[i]:
                if firstMinutes is None:
                    firstMinutes = i
                    preMinutes = i
                else:
                    # Clockwise diff and CounterClockwise diff
                    diff = min(i - preMinutes, MINS_IN_DAY - i + preMinutes)
                    minDiff = min(minDiff, diff)
                    preMinutes = i
        
        # Across midnight case
        diff = min(preMinutes - firstMinutes, MINS_IN_DAY - preMinutes + firstMinutes)
        minDiff = min(minDiff, diff)
        
        return minDiff