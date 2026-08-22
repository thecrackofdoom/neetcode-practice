class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = nums.index(0),nums.index(1),nums.index(2)
        nums[red],nums[0] = nums[0], nums[red]
        nums[white],nums[1] = nums[1], nums[white]
        nums[blue],nums[2] = nums[2], nums[blue]



        for i, num in enumerate(nums,3):
            if num == 0:
                if i == red + 1:
                    red = i
                else:
                    nums[red + 1], nums[i] = nums[i], nums[red + 1]
                    red += 1
            elif num == 1:
                if i == white + 1:
                    white = i
                else:
                    nums[white + 1], nums[i] = nums[i], nums[white + 1]
                    white += 1
            elif num == 2:
                if i == blue + 1:
                    blue = i
                else:
                    nums[blue + 1], nums[i] = nums[i], nums[blue + 1]
                    blue += 1
        