class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        allsq = []
        
        
        ans = []
        solution = []
        
        for row in range(n):
            
            for col in range(n):
                
                allsq.append((row, col))
            
        
        def coverage(qposi):
            dirs = [(1,1), (1, 0), (0, 1), (-1, 1)]
            cov = set()
            
            for dir in dirs:
                temp = qposi
                while 0 <= temp[0] + dir[0] <= n - 1 and 0 <= temp[1] + dir[1] <= n - 1:
                    temp = (temp[0] + dir[0], temp[1] + dir[1])
                    
                    cov.add(temp)
                
                temp = qposi
                while 0 <= temp[0] - dir[0] <= n - 1 and 0 <= temp[1] - dir[1] <= n - 1:
                    
                    temp = (temp[0] - dir[0], temp[1] - dir[1])
                    cov.add(temp)
                
            cov.add(qposi)
            
            
            return cov
        
        def backtracking(covered, qnum, qpos):
            '''if qpos and (qpos[0] == (0,1) or (qpos[0] == (0,0) and len(qpos) >= 2)):
                print(qpos,'\n', sorted(list(covered)))'''
            if qnum == 0 or len(qpos) == n:
                ans.append(qpos.copy())
                return
            if len(covered) == n * n and qnum > 0:
                return
            
            for square in [x for x in allsq if x not in covered]:
                if qpos == [] or square >= qpos[-1]:
                    qpos.append(square)
                    
                    new = coverage(square)
                    intersect = new & covered
                    covered.update(new)

                    

                    backtracking(covered, qnum - 1, qpos)

                    qpos.pop()
                    covered -= new
                    covered.update(intersect)

        
        backtracking(set(), n, [])
        
        
        
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
        


