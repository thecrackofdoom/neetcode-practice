class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0
        r = len(s) - 1
        while f < r:
            if not s[f].isalpha():
                f += 1
            if not s[r].isalpha():
                r -= 1
            if s[f].lower() != s[r].lower():
                return False
            f += 1
            r -= 1
        return True