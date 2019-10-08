'''
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive

Hi, here's your problem today. This problem was recently asked by Facebook:

You are given an array of integers. Return the smallest positive integer that is not present in the array. The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.
'''
def first_missing_positive(nums):
    i, n = 0, len(nums)
    while i<n:
        #Put the numbers into correct position in the array
        targetIdx = nums[i]-1
        if nums[i]>0 and targetIdx!=i and targetIdx<n and nums[targetIdx]!=nums[i]:
            #Should not use 'nums[i]-1' here for the list index
            nums[targetIdx], nums[i] = nums[i], nums[targetIdx]
        else:
            i+= 1
    for i in range(n):
        if nums[i]!=(i+1):
            return i+1
    return n+1

print(first_missing_positive([3, 4, -1, 1]))
# 2
