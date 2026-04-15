class Solution:
    def binary(self, nums, l, r, target):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            return -1
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        first = nums[0]
        last = nums[-1]
        l, r = 0, len(nums) - 1
        
        if first > last:
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < nums[mid - 1]:
                    rotation = mid
                    break
                elif nums[mid] >= first:
                    l = mid + 1
                else:
                    r = mid - 1
        else:
            return self.binary(nums, 0, len(nums) - 1, target)

        if target >= first:
            return self.binary(nums, 0, rotation - 1, target)
        else:
            return self.binary(nums, rotation, len(nums) - 1, target)