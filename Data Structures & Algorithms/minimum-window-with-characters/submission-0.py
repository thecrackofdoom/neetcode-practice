class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        have = {}
        need = {}

        for i, char in enumerate(t):
            need[char] = 1 + need.get(char, 0)

        l = 0
        substr = ""
        for r, char in enumerate(s):
            have[char] = 1 + have.get(char, 0)
            while all(have.get(key, 0) >= val for key, val in need.items()):
                if substr == "":
                    substr = s[l:r+1]
                elif len(substr) > r - l + 1:
                    substr = s[l:r+1]
                have[s[l]] -= 1
                l += 1
            
        return substr
            