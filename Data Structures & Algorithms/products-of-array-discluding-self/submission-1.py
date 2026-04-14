class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        for i, num in enumerate(nums):
            if i == 0:
                prefix.append(num)
            else:
                prefix.append(prefix[i - 1] * num)

        nums.reverse()
        for i, num in enumerate(nums):
            if i == 0:
                suffix.append(num)
            else:
                suffix.append(suffix[i - 1] * num)
        suffix.reverse()
        output = []
        print(prefix, suffix)
        for i in range(len(nums)):
            if i == 0:
                output.append(suffix[i+1])
            elif i == len(nums) - 1:
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1] * suffix[i+1])
        return output