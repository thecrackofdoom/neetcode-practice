class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        substr = {}
        perm = {}
        l = 0
        r = len(s1) - 1
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            substr[s1[i]] = 1 + substr.get(s1[i], 0)
            perm[s2[l:r+1][i]] = 1 + perm.get(s2[l:r+1][i], 0)
        while r < len(s2):
            if substr == perm:
                return True
            else:
                perm[s2[l]] -= 1
                if perm[s2[l]] == 0: del perm[s2[l]]
                l += 1
                r += 1
                if r == len(s2): return False
                perm[s2[r]] = 1 + perm.get(s2[r], 0)
        return False
