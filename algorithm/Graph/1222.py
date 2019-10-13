'''
1222. Queens That Can Attack the King
https://leetcode.com/contest/weekly-contest-158/problems/queens-that-can-attack-the-king/

On an 8x8 chessboard, there can be multiple Black Queens and one White King.
Given an array of integer coordinates queens that represents the positions of 
the Black Queens, and a pair of coordinates king that represent the position of 
the White King, return the coordinates of all the queens (in any order) that 
can attack the King.

Example 1:
Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:  
The queen at [0,1] can attack the king cause they're in the same row. 
The queen at [1,0] can attack the king cause they're in the same column. 
The queen at [3,3] can attack the king cause they're in the same diagnal. 
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.

Example 2:
Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
Output: [[2,2],[3,4],[4,4]]

Example 3:
Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]

Constraints:
1 <= queens.length <= 63
queens[0].length == 2
0 <= queens[i][j] < 8
king.length == 2
0 <= king[0], king[1] < 8
At most one piece is allowed in a cell.
'''
from typing import *

#Approach 1: O(num of queen)
#Queens can move in 8 directions.
#Start at the king's location and move in every direction until 
#either find a queen or reach the edge of the board.
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        queensSet = { (x,y) for x,y in queens }
        directions = [ (-1, 0), (1,0), ( 0,-1), (0, 1),
                       (-1,-1), (1,1), (-1, 1), (1,-1) ]
        for xd,yd in directions:
            x,y = king
            while 0 <= x < 8 and 0 <= y < 8:
                x += xd
                y += yd
                if (x,y) in queensSet:
                    ans.append([x, y])
                    break
        return ans

#Approach 2: O(num of queen)
#Loop throught all queens and update the nearest queue if the queen is in the 8 directions of the king.
# LU   U    RU 
#   ↖︎  ↑   ↗︎   
# L ← King → R 
#   ↙︎  ↓   ↘︎   
# LD   D    RD
#https://leetcode.com/problems/queens-that-can-attack-the-king/discuss/403852/Python-O(num-of-queen)-Readable-solution
class Solution2:
    def updatedict(self, dict, direction, thisdis, thispos):
        if direction in dict:
            (dis, pos) = dict[direction]
            if thisdis < dis:
                dict[direction] = (thisdis, thispos)
        else:
            dict[direction] = (thisdis, thispos)
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        dict = {}
        #kx, ky = king[0], king[1]  #No need to write index
        kx, ky = king               #Assign it directly
        for queen in queens:
            #qx, qy = queen[0], queen[1]  #No need to write index
            qx, qy = queen                #Assign it directly
            
            dx, dy = abs(qx-kx), abs(qy-ky)
            if dx == 0:    #qx == kx
                if qy < ky:
                    self.updatedict(dict, 'U', ky - qy, queen)
                else:
                    self.updatedict(dict, 'D', qy - ky, queen)
            elif dy == 0:   #qy == ky
                if qx < kx:
                    self.updatedict(dict, 'L', kx - qx, queen)
                else:
                    self.updatedict(dict, 'R', qx - kx, queen)
            elif dy == dx:
                if qy < ky and qx < kx:
                    self.updatedict(dict, 'LU', dy, queen)
                elif qy < ky and qx > kx:
                    self.updatedict(dict, 'RU', dy, queen)
                elif qy > ky and qx < kx:
                    self.updatedict(dict, 'LD', dy, queen)
                else:
                    self.updatedict(dict, 'RD', dy, queen)
        for queen in dict.values():
            (dis, pos) = queen
            ans.append(pos)
        return ans


print(Solution().queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0]))
#[[0,1],[1,0],[3,3]]
print(Solution().queensAttacktheKing([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], [3,3]))
#[[2,2],[3,4],[4,4]]
print(Solution().queensAttacktheKing([[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], [3,4]))
#[[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
