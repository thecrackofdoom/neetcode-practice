class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'(':')','[':']','{':'}'}
        for char in s:
            if char in pair:
                stack.append(char)
            else:
                if len(stack) == 0 or char != pair[stack[-1]]:
                    return False
                else:
                    stack.pop()
                    
        return True if len(stack) == 0 else False