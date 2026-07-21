class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        
        def dp(i):
            if i == 0:
                arr[i] = nums[i]
                return arr[i]
            if i == 1:
                arr[i] = max(nums[i], nums[0])
                return arr[i]
            if arr[i]:
                return arr[i]
            else:
                arr[i] = max(dp(i - 1), dp(i - 2) + nums[i])
                return arr[i]

        return dp(len(nums) - 1)