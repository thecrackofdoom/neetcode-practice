class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = [[0] * n for i in range(m)]
        map[2][3] = 1
        print(map)
        return 1