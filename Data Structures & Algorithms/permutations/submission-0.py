class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        state = [0] * len(nums)
        ans = []
        print(state)

        def backtracking(arr, state):
            if len(arr) == len(nums):
                ans.append(arr.copy())
                return
            print(arr, state)
            for index, s in enumerate(state):
                if s == 0:
                    arr.append(nums[index])
                    state[index] = 1
                    backtracking(arr, state)
                    arr.pop()
                    state[index] = 0
                    continue

                    
        
        backtracking([], state)

        return ans
