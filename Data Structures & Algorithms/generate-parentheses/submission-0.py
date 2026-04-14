class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtracking(open, close, arr):
            if open == close == n:
                ans.append(''.join(arr.copy()))
                return
            elif close > open:
                return
            if open < n:
                arr.append('(')
                backtracking(open + 1, close, arr)
                arr.pop()
            if open > close:
                arr.append(')')
                backtracking(open, close + 1, arr)
                arr.pop()
        backtracking(0, 0, [])
        return ans