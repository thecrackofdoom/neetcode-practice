class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtracking (i, arr, sum):
            if sum > target or i >= len(nums):
                return
            elif sum == target:
                ans.append(arr.copy())
                return
            arr.append(nums[i])
            backtracking(i, arr, sum + nums[i])
            arr.pop()
            backtracking(i + 1, arr, sum)
        backtracking(0 , [], 0)
        return ans