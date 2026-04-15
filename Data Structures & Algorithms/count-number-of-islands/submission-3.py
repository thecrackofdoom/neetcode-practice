class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        cnt = 0
        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return
            if grid[r][c] != '0':
                grid[r][c] = '0'
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
            return
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    cnt += 1
                    dfs(r,c)
        return cnt
            
