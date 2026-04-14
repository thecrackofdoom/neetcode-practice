class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0
        r = len(s) - 1
        while f < r:
            print(s[f].lower(), s[r].lower())
            while not s[f].isalnum() and f < r:
                f += 1
            while not s[r].isalnum() and r > f:
                r -= 1
            if s[f].lower() != s[r].lower():
                return False
            f += 1
            r -= 1
        return True