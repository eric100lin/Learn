'''
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a sorted list of numbers, change it into a balanced binary search tree. 
You can assume there will be no duplicate numbers in the list.
'''
from typing import *

from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value) + ' '
            nodes.append(node.left)
            nodes.append(node.right)
        return answer

class IndexSolution:
    def sortedArrayToBST(self, nums: List[int], left=None, right=None) -> TreeNode:
        if not nums:
            return None
        if left is None and right is None:
            left = 0
            right = len(nums)-1
        if left>right:
            return None
        mid = left + (right-left) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums, left, mid-1)
        node.right = self.sortedArrayToBST(nums, mid+1, right)
        return node

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

print(Solution().sortedArrayToBST([1, 2, 3, 4, 5, 6, 7]))
# 4261357
#   4
#  / \
# 2   6
#/ \ / \
#1 3 5 7

print(Solution().sortedArrayToBST([-10,-3,0,5,9]))
#     0
#    / \
#  -3   9
#  /   /
#-10  5