'''
1260. Shift 2D Grid
https://leetcode.com/contest/weekly-contest-163/problems/shift-2d-grid/

Given a 2D grid of size n * m and an integer k. You need to shift the grid k times.

In one shift operation:
Element at grid[i][j] becomes at grid[i][j + 1].
Element at grid[i][m - 1] becomes at grid[i + 1][0].
Element at grid[n - 1][m - 1] becomes at grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:
1 <= grid.length <= 50
1 <= grid[i].length <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
'''
from typing import *

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        height, width = len(grid), len(grid[0])
        # modulo total length to reduce shift
        # also ensure k in the len(nums)
        k %= (height * width)
        # serialize matrix to vector
        nums = [num for row in grid for num in row]
        # rotate vector with k shift
        nums = nums[-k:] + nums[:-k]
        # reconstruct matrix
        return [ nums[i : i+width] for i in range(0, len(nums), width)]

import copy
class NaiveSolution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        shifted = copy.deepcopy(grid)
        height, width = len(grid), len(grid[0])
        for shift in range(k):
            for h in range(height):
                for w in range(width):
                    ww = (w + 1) % width
                    wh = (h + (w + 1)//width) % height
                    shifted[wh][ww] = grid[h][w]
            grid = copy.deepcopy(shifted)
        return shifted

print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
# [[9,1,2],[3,4,5],[6,7,8]]
print(Solution().shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
# [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))
# [[1,2,3],[4,5,6],[7,8,9]]