class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
            print(stack)
            if not el.isalnum():
                print(el)

                if el == '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a+b)
                elif el == '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a-b)
                elif el == '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a*b)
                elif el == '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a/b))
                else:
                    stack.append(int(el))
            else:
                stack.append(int(el))
        return stack.pop()


        