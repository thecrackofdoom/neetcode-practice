class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = int(total/2)

        memo = [[-1] * (target + 1) for _ in range(len(nums))]
        print(memo)
        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i >= len(nums):
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            memo[i][target] = dfs(i + 1, cursum) or dfs(i + 1, cursum + nums[i])
            return memo[i][target] 
        return dfs(0, 0)