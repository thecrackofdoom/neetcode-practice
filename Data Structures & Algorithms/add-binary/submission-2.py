class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp = list(str(int(a) + int(b)))[::-1]
        print(temp)
        for index, digit in enumerate(temp):
            if digit == '2':
                if index == len(temp) - 1:
                    temp[index] = '0'
                    temp.append('1')
                else:
                    temp[index] = '0'
                    temp[index + 1] = str(int(temp[index + 1]) + 1)
        return ''.join(temp[::-1])
