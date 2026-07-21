class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        best = nums[0]

        for i, num in enumerate(nums[1:]):
            currMax = max(num, currMax * num, currMin * sum)
            currMin = min(num, currMax * num, currMin * sum)
            best = max(currMax, best)
        return best