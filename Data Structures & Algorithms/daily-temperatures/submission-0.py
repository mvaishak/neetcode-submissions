class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = {}

        for i in range(len(temperatures)):
            cur = temperatures[i]
            out[i] = 0
            if not stack:
                stack.append((cur,i))
            while stack and cur > stack[-1][0]:
                j = stack[-1][1]
                out[j] = i-j
                stack.pop()
            stack.append((cur,i))
        return list(out.values())


            