class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posdiag = set()
        negdiag = set()

        ans = []

        def backtracking(row, qpos):
            if len(qpos) == n:
                ans.append(qpos.copy())
                return
            for col in range(n):
                if col not in cols and col + row not in posdiag and col - row not in negdiag:
                    qpos.append((row,col))
                    cols.add(col)
                    posdiag.add(col + row)
                    negdiag.add(col - row)

                    backtracking(row + 1, qpos)

                    qpos.pop()
                    cols.discard(col)
                    posdiag.discard(col + row)
                    negdiag.discard(col - row)
        backtracking(0, [])
        solution = []
        for sol in ans:
            board = []
            for row in range(n):
                temp = []
                for col in range(n):
                    temp.append('.')
                board.append(temp)
            
            for queens in sol:
                board[queens[0]][queens[1]] = 'Q'
                print(board)
            for i in range(n):
                board[i] = ''.join(board[i])

            solution.append(board.copy())
        
        
        return solution
