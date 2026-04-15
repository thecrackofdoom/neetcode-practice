class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        increment = 0
        longest = 0
        i, j = 0 , 1
        while True:
            print(nums)
            if j == len(nums):
                break
            if nums[j] == nums[i] + 1:
                increment += 1
                i += 1
                j += 1
            else:
                if increment > longest:
                    longest = increment + 1
                increment = 0
                i = j + 1
                j = i + 1
        if increment > longest:
            return increment + 1
        else:
            return longest
            
