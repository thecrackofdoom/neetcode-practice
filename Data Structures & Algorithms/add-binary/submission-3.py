class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            temp = 0
            temp += int(a[i]) if i < len(a) else 0
            temp += int(b[i]) if i < len(b) else 0
            temp += carry
            
            carry = temp // 2
            temp = temp - 2 * carry
            print(temp, carry)
            res.append(str(temp))
            print(res)
        return ''.join(res[::-1])