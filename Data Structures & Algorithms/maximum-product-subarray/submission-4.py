class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        best = nums[0]

        for i, num in enumerate(nums[1:]):

            currMax = max(num, currMax * num, currMin * num)
            currMin = min(num, currMax * num, currMin * num)
            best = max(currMax, best)
        return best