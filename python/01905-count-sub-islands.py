def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    # Get the dimensions of the grids
    ROWS, COLS = len(grid1), len(grid1[0])

    # Initialize a set to keep track of visited cells
    visit = set()

    def dfs(r, c):
        # Base case: Check if we go out of bounds or encounter water
        if (
            r < 0
            or c < 0
            or r == ROWS
            or c == COLS
            or grid2[r][c] == 0
            or (r, c) in visit
        ):
            return True

        # Mark the cell as visited
        visit.add((r, c))
        res = True

        if grid1[r][c] == 0:
            res = False

        # Recursive DFS in all four directions
        res = dfs(r - 1, c) and res
        res = dfs(r + 1, c) and res
        res = dfs(r, c - 1) and res
        res = dfs(r, c + 1) and res

        return res

    # Initialize the count of sub-islands
    count = 0

    # Iterate through all cells in grid2
    for r in range(ROWS):
        for c in range(COLS):
            if grid2[r][c] and (r, c) not in visit and dfs(r, c):
                count += 1

    return count
