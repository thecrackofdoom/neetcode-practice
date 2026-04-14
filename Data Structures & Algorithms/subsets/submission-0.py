class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        l = len(nums)
        def subset(arr, index, length):
            if index >= length:
                self.ans.append(arr)
                return
            else:
                subset(arr, index + 1, length)
                
                subset(arr + [nums[index]], index + 1, length)
                
        subset([], 0, l)
        return self.ans
                