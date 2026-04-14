class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        l = 0
        maxL = 0
        for r in range(0, len(s)):
            if s[r] not in charDict:
                charDict[s[r]] = 1
            else:
                charDict[s[r]] += 1
            if k < (r - l + 1) - max(charDict.values()):
                charDict[s[l]] -= 1
                l += 1
            else:
                maxL = max(maxL, (r - l + 1))
        return maxL