# Runtime: 210ms
# MemoryUsage: 18.9MB

class Solution:
    def numIslands(self, grid):
        res, n, m = 0, len(grid), len(grid[0]) if grid else 0
        
        def dfs(i, j):
            grid[i][j] = "-1"
            if i > 0 and grid[i - 1][j] == "1": 
                dfs(i - 1, j)
            if j > 0 and grid[i][j - 1] == "1": 
                dfs(i, j - 1)
            if i + 1 < n and grid[i + 1][j] == "1": 
                dfs(i + 1, j)
            if j + 1 < m and grid[i][j + 1] == "1": 
                dfs(i, j + 1)
                
        for i in range(n): 
            for j in range(m):
                if grid[i][j] == "1": 
                    dfs(i, j) 
                    res += 1
        return res
