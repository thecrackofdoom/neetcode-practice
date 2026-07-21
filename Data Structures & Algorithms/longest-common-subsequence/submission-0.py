class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        arr = [[0] * n for i in range(m)]

        def dp(row, col):
            if row >= m or col >= n:
                return 0
            if arr[row][col]:
                return arr[row][col]
            else:
                if text1[row] == text2[col]:
                    arr[row][col] = 1 + dp(row + 1, col + 1)
                else:
                    arr[row][col] = max(dp(row + 1, col), dp(row, col + 1))
                return arr[row][col]
        return dp(0,0)