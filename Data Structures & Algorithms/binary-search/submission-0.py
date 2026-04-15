class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = int(len(nums)/2)
        if len(nums) == 0:
            return -1
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.search(nums[mid + 1:], target)
        else:
            return self.search(nums[:mid], target)

