class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        nums_first = nums[:-1]
        nums_first.append(0)
        nums_last = nums[1:]
        nums_last.insert(0, 0)
        print(nums_first,nums_last)
        
        dp_f = [-1] * n
        dp_l = [-1] * n
        def dfs(i, arr, dp):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            else:
                dp[i] = max(arr[i] + dfs(i+2,arr,dp), dfs(i+1,arr,dp))
                return dp[i]
        
        return max(dfs(0, nums_first, dp_f), dfs(0, nums_last, dp_l))