class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        best = nums[0]

        for num in nums[1:]:
            currMax = max(num, currMax * num, currMin * num)
            currMin = min(num, currMax * num, currMin * num)
            best = max(currMax, best)
            print(num, currMax, currMin, best)
        return best