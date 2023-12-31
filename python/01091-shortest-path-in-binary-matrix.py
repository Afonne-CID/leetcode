from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        N = len(grid)
        q = deque([(0, 0, 1)])  # (row, column, length)
        visit = set((0, 0))
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]

        while q:
            row, col, length = q.popleft()

            if (
                min(row, col) < 0 or
                max(row, col) >= N or
                grid[row][col]
            ):
                continue

            if row == N - 1 and col == N - 1:
                return length

            for dr, dc in directions:
                if (row + dr, col + dc) not in visit:
                    q.append((row + dr, col + dc, length + 1))
                    visit.add((row + dr, col + dc))

        return -1
