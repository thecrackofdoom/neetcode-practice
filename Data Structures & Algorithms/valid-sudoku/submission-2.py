class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            rSet = set()
            for col in range(9):
                if board[row][col] not in rSet:
                    rSet.add(board[row][col])
                elif board[row][col] != ".":
                    return False

        for col in range(9):
            cSet = set()
            for row in range(9):
                if board[row][col] not in cSet:
                    cSet.add(board[row][col])
                elif board[row][col] != ".":
                    return False
        '''
        for p in (0, 3, 6):
            squares = [set(),set(),set()]
            for row in range(p, p + 3):
                for q in (0, 3, 6):
                    for col in range(q, q + 3):
                        if board[row][col] not in squares[int(q/3)]:
                            squares[int(q/3)].add(board[row][col])
                        elif board[row][col] != ".":
                            return False
            print(squares) 
        '''
        squares = {}
        for row in range(9):
            for col in range(9):
                if (row//3, col//3) not in squares:
                    squares[(row//3, col//3)] = set()
                    squares[(row//3, col//3)].add(board[row][col])
                elif board[row][col] not in squares[(row//3, col//3)]:
                    squares[(row//3, col//3)].add(board[row][col])
                elif board[row][col] != ".":
                    return False
                print(squares)

        return True