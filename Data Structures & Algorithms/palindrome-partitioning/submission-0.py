class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def backtracking(start, curr, arr):
            if start >= len(s):
                ans.append(arr.copy())
                return
            elif curr >= len(s):
                return
            if s[start:curr + 1] == s[start:curr + 1][::-1]:
                arr.append(s[start:curr + 1])
                backtracking(curr + 1, curr + 1, arr)
                arr.pop()
            
            backtracking(start, curr + 1, arr)

        backtracking(0, 0, [])
        return ans
        