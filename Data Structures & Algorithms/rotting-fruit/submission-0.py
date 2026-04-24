class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c,0))

        minute = -1
        while q:
            cur = q.popleft()
            r = cur[0]
            c = cur[1]
            m = cur[2]
            

            if 0 <= r < ROWS and 0 <= c < COLS and (grid[r][c] == 1 or cur[2] == 0) and (r,c) not in visited:
                minute = max(minute, m)
                grid[r][c] = 2
                visited.add((r,c))
                
                q.append((r, c+1, m+1))
                q.append((r+1, c, m+1))
                q.append((r, c-1, m+1))
                q.append((r-1, c, m+1))
        
        check = set()
        for r in range(ROWS):
            check.update(grid[r])
        if 1 in check:
            return -1
        else:
            return minute
            


        