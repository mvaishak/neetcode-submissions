class MinStack: #performs getMin with O(1) instead of O(n) with brute force check

    def __init__(self):
        self.stack = []
        self.minimum = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum:
            self.minimum.append(min(val,self.minimum[-1]))
        else:
            self.minimum.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]