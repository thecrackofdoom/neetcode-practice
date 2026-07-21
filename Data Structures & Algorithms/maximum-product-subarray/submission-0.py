class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr = nums[0]
        best = nums[0]

        for i, num in enumerate(nums[1:]):
            curr = max(num, curr + num)
            best = max(curr, best)
        return best