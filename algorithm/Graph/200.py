'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), count the number of islands present in the grid. The definition of an island is as follows:
1.) Must be surrounded by water blocks.
2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
Assume all edges outside of the grid are water.

Example:
Input: 
10001
11000
10110
00000

Output: 3
'''
from typing import *

class Solution:
    def inRange(self, grid, j, i):
        numRow, numCol = len(grid), len(grid[0])
        if j < 0 or i < 0 or j >= numRow or i >= numCol:
            return False
        return True
    def dfsVisit(self, grid, visited, j, i):
        if not self.inRange(grid, j, i) or \
           grid[j][i]!="1" or visited[j][i]:
           return
        visited[j][i] = True
        self.dfsVisit(grid, visited, j-1, i)
        self.dfsVisit(grid, visited, j, i-1)
        self.dfsVisit(grid, visited, j+1, i)
        self.dfsVisit(grid, visited, j, i+1)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if grid and grid[0]:
            visited = [[False]*len(grid[0]) for _ in range(len(grid))]
            for j in range(len(grid)):
                for i in range(len(grid[j])):
                    if grid[j][i]=="1" and not visited[j][i]:
                        self.dfsVisit(grid, visited, j-1, i)
                        self.dfsVisit(grid, visited, j, i-1)
                        self.dfsVisit(grid, visited, j+1, i)
                        self.dfsVisit(grid, visited, j, i+1)
                        count += 1
        return count

print(Solution().numIslands([
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"],
]))
#1
print(Solution().numIslands([
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"],
]))
#3
print(Solution().numIslands([
["1","1","1"],
["0","1","0"],
["1","1","1"]
]))
#1