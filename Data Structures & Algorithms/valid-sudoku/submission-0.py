class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            rSet = {}
            for col in range(9):
                if board[row][col] not in rSet:
                    rSet[board[row][col]] = 1
                elif board[row][col] != ".":
                    return False

        for col in range(9):
            cSet = {}
            for row in range(9):
                if board[row][col] not in cSet:
                    cSet[board[row][col]] = 1
                elif board[row][col] != ".":
                    return False

        for p in (0, 3, 6):
            squares = [{},{},{}]
            for row in range(p, p + 3):
                for q in (0, 3, 6):
                    for col in range(q, q + 3):
                        if board[row][col] not in squares[int(q/3)]:
                            squares[int(q/3)][board[row][col]] = 1
                        elif board[row][col] != ".":
                            return False
            print(squares)


        return True