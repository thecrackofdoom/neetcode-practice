class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,1
        maxL = 0
        while r <= len(s):
            if len(s[l:r]) == len(set(s[l:r])):
                maxL = max(maxL, len(s[l:r]))
                r += 1
            else:
                l += 1
        return maxL