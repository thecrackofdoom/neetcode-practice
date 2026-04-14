class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[-1]

        l, r = 0, len(nums) - 1
        first = nums[0]
        last = nums[-1]

        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] >= first:
                l = mid + 1
            elif nums[mid] <= last:
                r = mid - 1
        