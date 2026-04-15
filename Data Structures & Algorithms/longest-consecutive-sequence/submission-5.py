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
            print(j)
            if j == len(nums) + 1:
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
            longest = increment + 1
            return longest
        else:
            return longest
            
