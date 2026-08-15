class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ptr = 0
        if not strs:
            return ""
        while True:
            curr = string[ptr]
            for string in strs:
                if string[ptr] != curr:
                    return string[:ptr+1]
            ptr += 1
            