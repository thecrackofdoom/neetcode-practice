class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ptr = 0
        if not strs:
            return ""
        ans = None
        min_len = min([len(x) for x in strs])
        if min_len == 0:
            return ""
        while ptr < min_len:
            curr = strs[0][ptr]
            for string in strs:
                if string[ptr] != curr:
                    return string[:ptr]
                ans = string[:ptr+1]
            ptr += 1
        return ans