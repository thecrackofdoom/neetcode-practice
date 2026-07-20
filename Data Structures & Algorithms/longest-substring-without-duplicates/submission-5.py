class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        charset = set()
        max_len = 0
        
        if not s:
            return  0

        while right < len(s):
            if s[right] not in charset:
                charset.add(s[right])
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                charset.remove(s[left])
                left += 1
        return max_len