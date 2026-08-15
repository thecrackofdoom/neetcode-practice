class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ptr = 0
        if not any(strs):
            return ""
        ans = None
        while ptr < min([len(x) for x in strs]):
            curr = strs[0][ptr]
            for string in strs:
                if string[ptr] != curr:
                    return string[:ptr]
                ans = string[:ptr+1]
            ptr += 1
        return ans