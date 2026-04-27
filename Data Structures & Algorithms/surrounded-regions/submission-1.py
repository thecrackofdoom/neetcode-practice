class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS) :
                return
            if board[r][c] == 'X' or board[r][c] == 'I':
                return
            board[r][c] = 'I'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS- 1 or c == 0 or c == COLS - 1:
                    if board[r][c] == 'O':
                        dfs(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'I':
                    board[r][c] = 'O'