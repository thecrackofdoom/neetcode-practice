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
                if nums[l] + nums[r] == -nums[i]:
                    ans.append([nums[l], nums[r], nums[i]])
                    break
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1
        
        return ans