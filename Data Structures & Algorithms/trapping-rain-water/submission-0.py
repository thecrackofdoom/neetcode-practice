class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left = []
        right = []
        water = 0
        while l < len(height):
            if l == 0 or r == len(height) - 1:
                left.append(height[l])
                right.append(height[r])
                l += 1
                r -= 1
            if height[l] < left[-1]:
                left.append(left[-1])
            else:
                left.append(height[l])
            if height[r] < right[-1]:
                right.append(right[-1])
            else:
                right.append(height[r])
            l += 1
            r -= 1
        for i in range(len(height)):
            water += min(left[i], right[len(height) - 1 - i]) - height[i]
        print(left)
        print(list(reversed(right)))
        return water