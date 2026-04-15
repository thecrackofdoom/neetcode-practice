class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isalnum():
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                match token:
                    case '+':
                        stack.append(a+b)
                    case '-':
                        stack.append(b-a)
                    case '*':
                        stack.append(int(a*b))
                    case '/':
                        stack.append(int(b/a))
        return stack[0]