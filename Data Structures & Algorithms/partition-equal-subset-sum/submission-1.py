class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = int(total/2)
        def dfs(i, cursum):
            if cursum == target:
                return True
            if cursum > target or i >= len(nums):
                return False
            return dfs(i + 1, cursum) or dfs(i + 1, cursum + nums[i])
        return dfs(0, 0)