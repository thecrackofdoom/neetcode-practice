class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        
        dirs = [(0, 1),(1, 0),(0, -1),(-1, 0)]

        r, c = 0, 0
        
        cur = 1
        mat[r][c] = 1

        while cur < int(n*n):
            for dir in dirs:
                while True:
                    if 0 <= r + dir[0] < n and 0 <= c + dir[1] < n and mat[r + dir[0]][c + dir[1]] == 0:
                        r += dir[0]
                        c += dir[1]
                    else:
                        break
                    cur += 1
                    mat[r][c] = cur
        return mat