class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "*" + string
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        str_len = ""
        i = 0
        print(s)
        while True:
            print(decoded)
            if s[i] == "*":
                decoded.append(s[i + 1: i + int(str_len) + 1])
                i += int(str_len) + 1
                str_len = ""
                if i == len(s):
                    return decoded
            else:
                str_len += s[i]
                i += 1