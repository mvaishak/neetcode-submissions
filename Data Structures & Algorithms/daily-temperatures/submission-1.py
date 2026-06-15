class Solution: ##This is like my previous approach but more optimized
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        out = [0]*n
        for i in range(n):
            cur = temperatures[i]
            while stack and cur > stack[-1][0]:
                j = stack[-1][1]
                out[j] = i-j
                stack.pop()
            stack.append((cur,i))
        return out


            