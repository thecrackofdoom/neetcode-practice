class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtracking(i, arr, sum):
            if sum == target:
                ans.append(arr.copy())
                return
            elif sum > target or i >= len(candidates):
                return
            
            arr.append(candidates[i])
            backtracking(i + 1, arr, sum + candidates[i])
            arr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
 
            backtracking(i + 1, arr, sum)
        backtracking(0, [], 0)
        return ans