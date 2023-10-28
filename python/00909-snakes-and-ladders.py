from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]) -> int:
        length = len(board)
        board.reverse()  # Reverse the board to simplify indexing

        # Helper function to convert square number to row, column coordinates
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]

        # Initialize a queue for BFS
        q = deque()
        q.append([1, 0])  # [square, moves]
        visit = set()  # Keep track of visited squares

        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)

                # Check if there's a snake or ladder at this square
                if board[r][c] != -1:
                    nextSquare = board[r][c]

                # If we reach the last square, return the number of moves
                if nextSquare == length * length:
                    return moves + 1



 # If we haven't visited this square before, add it to the queue
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])

        return -1  # If we can't reach the end

# Example usage
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
solution = Solution()
print(solution.snakesAndLadders(board))  # Output: 4
