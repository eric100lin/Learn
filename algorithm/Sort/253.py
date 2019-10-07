'''
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/
https://www.youtube.com/watch?v=PWgFnSygweI

Hi, here's your problem today. This problem was recently asked by Google:

You are given an array of tuples (start, end) representing time intervals for lectures. The intervals may be overlapping. Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
'''
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import heapq
def minmalMeetingRooms(intervals):
    if not intervals:
        return 0
    intervals = sorted(intervals, key=lambda it: it.start)
    minHeap = []
    heapq.heappush(minHeap, intervals[0].end)
    for i in range(1, len(intervals)):
        current = intervals[i]
        elariestEnd = heapq.heappop(minHeap)
        if current.start >= elariestEnd:
            elariestEnd = current.end
        else:
            heapq.heappush(minHeap, current.end)
        heapq.heappush(minHeap, elariestEnd)
    return len(minHeap)


import unittest

class TestIntervals(unittest.TestCase):

    def testExample1(self):
        intervals = []
        intervals.append(Interval(30, 75))
        intervals.append(Interval(0, 50))
        intervals.append(Interval(60, 150))
        self.assertEqual(minmalMeetingRooms(intervals), 2)

    def testExample2(self):
        intervals = []
        intervals.append(Interval(7, 10))
        intervals.append(Interval(2, 4))
        self.assertEqual(minmalMeetingRooms(intervals), 1)

    def testEdge(self):
        intervals = []
        intervals.append(Interval(1, 2))
        intervals.append(Interval(2, 4))
        intervals.append(Interval(3, 5))
        intervals.append(Interval(5, 6))
        intervals.append(Interval(4, 6))
        self.assertEqual(minmalMeetingRooms(intervals), 2)

    def testSameStart(self):
        intervals = []
        intervals.append(Interval(1, 2))
        intervals.append(Interval(1, 4))
        intervals.append(Interval(1, 5))
        intervals.append(Interval(1, 6))
        self.assertEqual(minmalMeetingRooms(intervals), 4)

if __name__ == "__main__":
    unittest.main()
