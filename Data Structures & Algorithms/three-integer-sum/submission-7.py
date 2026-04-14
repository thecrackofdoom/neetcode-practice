class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                if nums[l] + nums[r] == -nums[i]:
                    ans.append([nums[l], nums[r], nums[i]])
                    l+= 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
        return ans