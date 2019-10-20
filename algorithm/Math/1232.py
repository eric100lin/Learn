'''
1232. Check If It Is a Straight Line
https://leetcode.com/contest/weekly-contest-159/problems/check-if-it-is-a-straight-line/

You are given an array coordinates, 
coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
'''
from typing import *

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        firstX, firstY = coordinates[0]
        secondX, secondY = coordinates[1]
        dx, dy = secondX-firstX, secondY-firstY
        for i in range(2, len(coordinates)):
            pointX, pointY = coordinates[i]
            pdx, pdy = pointX-firstX, pointY-firstY
            # Slop = dy/dx
            # Slope1=Slope2 => dy1/dx1=dy2/dx2 => dx1*dy2=dx2*dy1
            if pdx * dy != pdy * dx:
                return False
        return True

# Ugly
class SolutionUgly:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        firstX, firstY = coordinates[0]
        secondX, secondY = coordinates[1]
        if secondX-firstX == 0:
            sloop = None
        else:
            sloop = (secondY-firstY)/(secondX-firstX)
        ans = True
        for i in range(2, len(coordinates)):
            pointX,pointY = coordinates[i]
            if sloop is None and (pointX-firstX)!=0:
                ans = False
                break
            else:
                sloopi = (pointY-firstY)/(pointX-firstX)
                if sloopi != sloop:
                    ans = False
                    break
        return ans

print(Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))