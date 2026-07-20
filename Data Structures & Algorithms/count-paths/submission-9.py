class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = [[0] * n for i in range(m)]
        
        def path(row, col):
            if row == 0 or col == 0:
                map[row][col] = 1
                return 1
            if map[row][col] > 0:
                return map[row][col]
            map[row][col] = path(row -1, col) + path(row, col - 1)

            return map[row][col]
        
        
        return path(m-1, n-1)
        