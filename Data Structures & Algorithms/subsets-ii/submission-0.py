class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtracking(arr, i):
            if i >= len(nums): 
                ans.append(arr.copy())
                return
            
            arr.append(nums[i])
            backtracking(arr, i + 1)

            arr.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtracking(arr, i + 1)

        backtracking([], 0)
        return ans