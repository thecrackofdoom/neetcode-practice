class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        ans_hash = []
        def dupe(arr):
            hash = {}
            for num in arr:
                hash[num] = 1 + hash.get(num, 0)
            
            for existing in ans_hash:
                if hash == existing:
                    return False
                else:
                    continue

            return True
        def addhash(arr):
            hash = {}
            for num in arr:
                hash[num] = 1 + hash.get(num, 0)

            ans_hash.append(hash)

        def backtracking(curr_arr):
            if sum(curr_arr) > target:
                return
            elif sum(curr_arr) == target:
                if dupe(curr_arr):
                    addhash(curr_arr)
                    ans.append(curr_arr.copy())
                return
            for num in nums:
                curr_arr.append(num)
                backtracking(curr_arr)
                curr_arr.pop()
        backtracking([])
        return ans