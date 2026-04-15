class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'(':')','[':']','{':'}'}
        for char in s:
            if char in pair:
                stack.append(char)
            else:
                if char == pair[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False