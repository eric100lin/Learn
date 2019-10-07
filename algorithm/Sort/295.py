'''
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Hi, here's your problem today. This problem was recently asked by Google:

You are given a stream of numbers. Compute the median for each new element .

Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
'''
from typing import *

import heapq
def running_median(stream):
    medians = []
    maxHeap = []
    minHeap = []
    for num in stream:
        if not maxHeap or num <= -maxHeap[0]:
            heapq.heappush(maxHeap, -num)
            if len(maxHeap) - len(minHeap) > 1:
                max = - heapq.heappop(maxHeap)
                heapq.heappush(minHeap, max)
        else:
            heapq.heappush(minHeap, num)
            if len(minHeap) > len(maxHeap):
                min = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -min)

        if len(maxHeap) != len(minHeap):
            median = -maxHeap[0]
        else:
            max = -maxHeap[0]
            min = minHeap[0]
            median = (max + min)/2
        medians.append(median)
    return medians

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
            if len(self.maxHeap) - len(self.minHeap) > 1:
                max = - heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, max)
        else:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > len(self.maxHeap):
                min = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -min)

    def findMedian(self) -> float:
        if len(self.maxHeap) != len(self.minHeap):
            median = -self.maxHeap[0]
        else:
            max = -self.maxHeap[0]
            min = self.minHeap[0]
            median = (max + min)/2
        return median

import unittest

class TestRunningMedian(unittest.TestCase):

    def testExample1(self):
        medians = running_median([2, 1, 4, 7, 2, 0, 5])
        self.assertEqual(medians, [2, 1.5, 2, 3.0, 2, 2.0, 2])

    def testExample2(self):
        medians = running_median([1, 2, 3])
        self.assertEqual(medians, [1, 1.5, 2])

class TestMedianFinder(unittest.TestCase):

    def testExample1(self):
        input = [2, 1, 4, 7, 2, 0, 5]
        expectMedians = [2, 1.5, 2, 3.0, 2, 2.0, 2]
        mf = MedianFinder()
        for i,m in zip(input,expectMedians):
            mf.addNum(i)
            self.assertEqual(mf.findMedian(), m)

    def testExample2(self):
        input = [1, 2, 3]
        expectMedians = [1, 1.5, 2]
        mf = MedianFinder()
        for i,m in zip(input,expectMedians):
            mf.addNum(i)
            self.assertEqual(mf.findMedian(), m)

    def testExample3(self):
        input = [41, 35, 62, 4, 97, 108]
        expectMedians = [41, 38, 41, 38, 41, 51.5]
        mf = MedianFinder()
        for i,m in zip(input,expectMedians):
            mf.addNum(i)
            self.assertEqual(mf.findMedian(), m)

if __name__ == "__main__":
    unittest.main()