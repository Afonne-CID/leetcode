def islandPerimeter(self, grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 1
        if grid[i][j] == -1:
            return 0
        grid[i][j] = -1
        perim = 0
        perim += dfs(i + 1, j)
        perim += dfs(i - 1, j)
        perim += dfs(i, j + 1)
        perim += dfs(i, j - 1)
        return perim

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i, j)
