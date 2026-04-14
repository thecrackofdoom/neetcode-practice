class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])
        dirs = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        r, c = 0, 0
        ans.append(matrix[r][c])
        matrix[r][c] = -101
        while len(ans) < int(rows * cols):
            for dir in dirs:
                while True:
                    if 0 <= r + dir[0] < rows and 0 <= c + dir[1] < cols and matrix[r + dir[0]][c + dir[1]] != -101:
                        r += dir[0]
                        c += dir[1]
                    else:
                        break
                    ans.append(matrix[r][c])
                    matrix[r][c] = -101
                    
        return ans
