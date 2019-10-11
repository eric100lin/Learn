'''
5181. Distance Between Bus Stops
https://leetcode.com/contest/weekly-contest-153/problems/distance-between-bus-stops/

A bus has n stops numbered from 0 to n - 1 that form a circle. 
We know the distance between all pairs of neighboring stops where 
distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.
Return the shortest distance between the given start and destination stops.

Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.

Constraints:
    1 <= n <= 10^4
    distance.length == n
    0 <= start, destination < n
    0 <= distance[i] <= 10^4
'''
from typing import *

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        dc, dcc = 0, 0
        clockwise = start
        counterclockwise = destination
        while clockwise != destination and counterclockwise != start:
            dc += distance[clockwise]
            clockwise = (clockwise + 1) % n
            dcc += distance[counterclockwise]
            counterclockwise = (counterclockwise + 1) % n
        if clockwise == destination and counterclockwise == start:
            return min(dc, dcc)
        elif clockwise == destination:
            return dc
        elif counterclockwise == start:
            return dcc
        return 0

print(Solution().distanceBetweenBusStops([1,2,3,4], 0, 1))
#1
print(Solution().distanceBetweenBusStops([1,2,3,4], 0, 2))
#3
print(Solution().distanceBetweenBusStops([1,2,3,4], 0, 3))
#4