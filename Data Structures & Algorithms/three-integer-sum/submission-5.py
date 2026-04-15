class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        checked = set()
        nums = list(sorted(nums))
        ans = []
        for i in range(len(nums)):
            if nums[i] in checked:
                continue
            else:
                checked.add(nums[i])
            print(i)
            l = 0
            r = len(nums) - 1
            
            while l < r:
                if l == i:
                    l += 1
                    continue
                elif r == i:
                    r -= 1
                    continue
                if nums[l] + nums[r] == -nums[i]:
                    ans.append([nums[l], nums[r], nums[i]])
                    break
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1
        
        return ans