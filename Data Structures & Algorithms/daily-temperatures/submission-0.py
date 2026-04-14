class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            temp_ans = []
            if i == 0:
                stack.append([i, temp])
                continue
            print(stack)
            if not stack:
                stack.append([i, temp])
            elif temp <= stack[-1][1]:
                stack.append([i, temp])
            else:
                while stack and temp > stack[-1][1]:
                    prev_temp = stack.pop()
                    ans[prev_temp[0]] = i - prev_temp[0]
                stack.append([i, temp])

        return ans
        