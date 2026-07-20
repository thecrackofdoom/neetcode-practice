class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = [[0] * n for i in range(m)]
        
        def path(row, col):
            if row == 0 or col == 0:
                map[row][col] = 1
                return 1
            map[row][col] = map[row - 1][col] + map[row][col - 1]

            return map[row][col]
        
        print(path(m-1, n-1))
        return 1
        