class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_idx = 0
        max_len = -1
        for i in range(len(s)):
            l,r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_idx = l
                    max_len = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_idx = l
                    max_len = r - l + 1
                l -= 1
                r += 1
                
        return s[max_idx:max_idx + max_len]