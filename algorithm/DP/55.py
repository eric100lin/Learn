'''
55. Jump Game
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, 
you are initially positioned at the first index of the array.
Each element in the array represents your maximum 
jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: 
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: 
You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, 
which makes it impossible to reach the last index.
'''
from typing import *

# Approach 1: just recursive
class Solution1:
    def canJumpFromPosition(self, position, nums: List[int]):
        if position == len(nums) - 1:
            return True
        furthestJump = min(len(nums)-1, position+nums[position])
        for nextPosition in range(furthestJump, position, -1):
            if self.canJumpFromPosition(nextPosition, nums):
                return True
        return False
    def canJump(self, nums: List[int]) -> bool:
        return self.canJumpFromPosition(0, nums)

# Approach 2: Top-down DP
# Once we determine that a certain index is good / bad, 
# this result will never change
import enum
class IndexType(enum.Enum):
    UNKONW = 1
    GOOD = 2
    BAD = 3

class Solution2:
    def canJumpFromPosition(self, position, nums, memo):
        if memo[position] != IndexType.UNKONW:
            return memo[position] == IndexType.GOOD
        furthestJump = min(len(nums)-1, position+nums[position])
        for nextPosition in range(furthestJump, position, -1):
            if self.canJumpFromPosition(nextPosition, nums, memo):
                memo[position] = IndexType.GOOD
                return True
        memo[position] = IndexType.BAD
        return False
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        memo = [IndexType.UNKONW] * len(nums)
        memo[-1] = IndexType.GOOD
        return self.canJumpFromPosition(0, nums, memo)

# Approach 3: Bottom-up DP
class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        memo = [IndexType.UNKONW] * len(nums)
        memo[-1] = IndexType.GOOD
        for idx in range(len(nums)-2, -1, -1):
            furthestJump = min(len(nums)-1, idx+nums[idx])
            for position in range(furthestJump, idx, -1):
                if memo[position] == IndexType.GOOD:
                    memo[idx] = IndexType.GOOD
                    break
            else:
                memo[idx] = IndexType.BAD
        return memo[0] == IndexType.GOOD

# Approach 4: Greedy
# only keep track left-most GOOD position
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for idx in range(len(nums)-1,-1,-1):
            # Use ">= lastPos" to check can reach
            # left-most GOOD position
            if idx + nums[idx] >= lastPos:
                lastPos = idx
        return lastPos == 0

print(Solution().canJump([5,4,3,2,1,0,0]))
# False, worst case, all combinations will be tried

print(Solution().canJump([1,5,2,1,0,2,0]))
# True, 0 -> 1 -> 6

print(Solution().canJump([2,3,1,1,4]))
# True, 0 -> 1 -> 4

print(Solution().canJump([3,2,1,0,4]))
# False

print(Solution().canJump([0]))
# True

print(Solution().canJump([1]))
# True

print(Solution().canJump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))
# True

print(Solution().canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))
# False