class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        queue = deque()

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c,0))
        
        
        while queue:
            
            cur = queue.popleft()
            r = cur[0]
            c = cur[1]
            step = cur[2]

            
            if 0 <= r < ROWS and 0 <= c < COLS and (grid[r][c] == 2147483647 or step == 0):
                grid[r][c] = step
            
                queue.append((r, c+1, step+1))
                queue.append((r+1, c, step+1))
                queue.append((r, c-1, step+1))
                queue.append((r-1, c, step+1))
        
                
                    
