class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ans = False

        def backtracking(visited, pos, index):
            if index >= len(word):
                print("true")
                self.ans = True
                print(self.ans)
                return True
            if len(visited) == len(board) * len(board[0]):
                return
            if pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board[0]):
                return
            elif board[pos[0]][pos[1]] != word[index]:
                return
            else:
                visited.add(pos)
                print(index)
                if (pos[0]+1, pos[1]) not in visited:
                    backtracking(visited, (pos[0]+1, pos[1]), index + 1)

                if (pos[0]-1, pos[1]) not in visited:
                    backtracking(visited, (pos[0]-1, pos[1]), index + 1)

                if (pos[0], pos[1]+1) not in visited:
                    backtracking(visited, (pos[0], pos[1]+1), index + 1)

                if (pos[0], pos[1]-1) not in visited:
                    backtracking(visited, (pos[0], pos[1]-1), index + 1)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                backtracking(set(), (row,col), 0)
                if self.ans:
                    return self.ans
        
        return self.ans

