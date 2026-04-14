class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def dfs(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            else:
                temp = 0
                for x in range(i + 2, n):
                    temp = max(temp, dfs(x))
                    print(temp)

                dp[i] = max( nums[i] + temp, dfs(i + 1))
                
                return dp[i]
        dfs(0)
        
        return max(dp)
