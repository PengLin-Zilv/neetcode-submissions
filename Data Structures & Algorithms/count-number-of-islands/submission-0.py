class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        # set m to # of rows, n to # of columns

        if not grid: 
            return 0

        def dfs(i,j):
            # this dfs turns all the island to 0

            # guard: check bound and check valid cell
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] != "1":
                return
            
            # now we have valid cell, let's turn them to 0
            grid[i][j] = "0"

            dfs(i-1, j) # check up
            dfs(i+1, j) # check down
            dfs(i, j-1) # check left
            dfs(i, j+1) # check right

        num_islands = 0
        # now we go to each cell run dfs
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i,j)
        return num_islands