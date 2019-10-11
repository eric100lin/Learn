'''
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Hi, here's your problem today. This problem was recently asked by Uber:

You have a landscape, in which puddles can form. 
You are given an array of non-negative integers representing 
the elevation at each location. 
Return the amount of water that would accumulate if it rains.

For example: 
[0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
       X               
   X███XX█X              
 X█XX█XXXXXX                   
# [0,1,0,2,1,0,1,3,2,1,2,1]
'''
from typing import *

#wrong
def wrong_capacity(arr):
    acc = 0
    for i in range(1, len(arr)-1):
        l,r = i-1, i+1
        base = arr[i]
        while arr[l]>arr[i] and arr[r]>arr[i]:
            height = min(arr[l],arr[r])
            acc += (r-l-1) * (height-base)
            base = height
            if l==0 and r==len(arr)-1:
                break
            if l!=0:
                l-=1
            if r!=len(arr)-1:
                r+=1
    return acc

class Solution:
    def trap(self, height: List[int]) -> int:
        acc, left, right = 0, 0, len(height)-1
        maxHeightL, maxHeightR = 0, 0
        while left < right:
            if height[left]<height[right]:
                #Same height or larger than max will not acc water
                if height[left] >= maxHeightL:
                    maxHeightL = height[left]
                else:
                    acc += maxHeightL - height[left]
                left += 1
            else:
                if height[right] >= maxHeightR:
                    maxHeightR = height[right]
                else:
                    acc += maxHeightR - height[right]
                right -= 1
        return acc

print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
print(Solution().trap([2,1,0,2]))
# 3
print(Solution().trap([5,2,1,2,1,5]))
# 14
