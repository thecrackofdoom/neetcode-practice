class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 1
        max_str = ''
        for i in range(len(s)):
            l,r = i, i
            while 0 <= l-1 < len(s) and 0 <= r+1 < len(s) and s[l-1] == s[r+1]:
                l -= 1
                r += 1
                max_str = s[l:r+1] if r - l + 1 > len(max_str) else max_str
            
            l, r = i, i + 1
            while 0 <= l < len(s) and 0 <= r < len(s) and s[l] == s[r]:
                max_str = s[l:r+1] if r - l + 1 > len(max_str) else max_str
                l -= 1
                r += 1
                
        return max_str