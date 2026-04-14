class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums = sorted(list(set(nums)))
        if len(nums) < 2:
            return(len(nums))
        increment = 0
        longest = 0
        i, j = 0 , 1
        while True:
            print(nums)
            print(increment)
            if j == len(nums):
                break
            if nums[j] == nums[i] + 1:
                increment += 1
                i += 1
                j += 1
            else:
                if increment + 1 > longest:
                    longest = increment + 1
                increment = 0
                i = j
                j += 1
        if increment + 1 > longest:
            longest = increment + 1
            return longest
        else:
            return longest
            
