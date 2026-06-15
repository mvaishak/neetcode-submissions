class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        a = ''
        b= ''
        for char in s:
            if len(stack)==0:
                stack.append(char)
            else:
                a = stack[-1]
                b = char
                if a == '(' and b== ')':
                    stack.pop()
                elif a == '{' and b== '}':
                    stack.pop()
                elif a=='[' and b==']':
                    stack.pop()
                else:
                    stack.append(b)
        return len(stack) == 0