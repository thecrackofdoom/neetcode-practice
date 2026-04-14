class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pointer = 0

        while nums[pointer] > 0:
            nums[pointer] = -nums[pointer]
            print(nums[pointer])
            pointer = -nums[pointer]
            
        return pointer