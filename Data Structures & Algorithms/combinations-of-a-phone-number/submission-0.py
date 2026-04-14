class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad = {2: ['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'],
         5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r', 's'],
         8: ['t','u','v'], 9: ['w','x','y', 'z']}
        ans = []
        if digits == "":
            return []
        def backtracking(arr, index):
            if len(arr) == len(digits):
                ans.append(''.join(arr))
                return
            for char in numpad[int(digits[index])]:
                arr.append(char)
                backtracking(arr, index + 1)
                arr.pop()
        backtracking([], 0)
        return ans
