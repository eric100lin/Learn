'''
348. Design Tic-Tac-Toe
https://leetcode.com/problems/design-tic-tac-toe/

Hi, here's your problem today. 
This problem was recently asked by Google:

Design a Tic-Tac-Toe game played between 
two players on an n x n grid. 
A move is guaranteed to be valid, 
and a valid move is one placed on an empty block in the grid. 
A player who succeeds in placing n of their marks in 
a horizontal, diagonal, or vertical row wins the game. 
Once a winning condition is reached, 
the game ends and no more moves are allowed. 
Below is an example game which ends in a winning condition:

Given n = 3, assume that player 1 is "X" and player 2 is "O" 
board = TicTacToe(3);

board.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

board.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

board.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

board.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

board.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

board.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

board.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
'''
from typing import *

#O(n square), check each cell in row, col and diagonal
class TicTacToe:
    def __init__(self, n: int):
        # Fill this in.
        self.board = [[0]*n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        # Fill this in.
        self.board[col][row] = player
        N = len(self.board)

        # Only need to chek same row 
        # (no need to check other rows)
        for y in range(N):
            if self.board[y][row] != player:
                break
        else:
            # Only return True if no break
            return player

        # Only need to chek same col 
        # (no need to check other cols)
        for x in range(N):
            if self.board[col][x] != player:
                break
        else:
            return player

        # Check diagonal (LeftTop to RightBottom)
        if col == row:
            for yx in range(N):
                if self.board[yx][yx] != player:
                    break
            else:
                return player

        # Check diagonal (RightTop to LeftBottom)
        if col+row == N-1:
            for yx in range(N):
                if self.board[N-1-yx][yx] != player:
                    break
            else:
                return player
        
        return 0

#O(n), sum for each row, col and diagonal
class TicTacToeSum:
    def __init__(self, n):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antiDiagonal = 0
    
    def move(self, row, col, player):
        value = 1 if player==1 else -1
        N = len(self.rows)
        
        self.rows[row] += value
        self.cols[col] += value
        if row == col:
            self.diagonal += value
        if row + col == N - 1:
            self.antiDiagonal += value
        
        wins = 0
        for sum in (self.rows[row], self.cols[col], self.diagonal, self.antiDiagonal):
            if sum == N:
                # player1 wins
                wins = 1
            elif sum == -N:
                # player2 wins
                wins = 2
        return wins

board = TicTacToe(3)
print(board.move(0, 0, 1))
print(board.move(0, 2, 2))
print(board.move(2, 2, 1))
print(board.move(1, 1, 2))
print(board.move(2, 0, 1))
print(board.move(1, 0, 2))
print(board.move(2, 1, 1))