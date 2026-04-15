class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        
        def dfs(i, containFirst):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            else:
                if containFirst:
                    dp[i] = max(nums[i] + dfs(i + 2, containFirst) if i+2 != n-1 else 0, dfs(i + 1, False))
                else:
                    dp[i] = max(nums[i] + dfs(i + 2, False), dfs(i + 1, False))
                return dp[i]
        return dfs(0, True)