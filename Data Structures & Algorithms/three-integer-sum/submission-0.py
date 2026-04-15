class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        l = 0
        r = len(nums) - 1
        ans = []
        while l < r:
            if -(nums[l] + nums[r]) in set(nums[l+1:r]):
                ans.append([-(nums[l] + nums[r]), nums[l], nums[r]])
                l += 1
                continue
            elif nums[l] + nums[r] > 0:
                r -= 1
            elif nums[l] + nums[r] < 0:
                l += 1
        return ans
