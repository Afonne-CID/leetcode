def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    # Get the number of rows and columns in the grid.
    ROWS, COLS = len(grid), len(grid[0])

    # Create a set to keep track of visited cells.
    visit = set()

    def dfs(r, c):
        # Base cases:
        # If we go out of bounds, return 0.
        if (
            r < 0
            or r == ROWS
            or c < 0
            or c == COLS
            or grid[r][c] == 0
            or (r, c) in visit
        ):
            return 0

        # Mark the cell as visited.
        visit.add((r, c))

        # Recursively explore all four directions.
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    # Initialize the maximum area to 0.
    area = 0

    # Iterate through the entire grid to find the maximum area.
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                area = max(area, dfs(r, c))

    # Return the maximum island area.
    return area
