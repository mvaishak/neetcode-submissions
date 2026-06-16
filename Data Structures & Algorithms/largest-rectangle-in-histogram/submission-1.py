class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max_area = 0
        for i in range(len(heights)):
            while stack and (heights[stack[-1]] > heights[i]) :
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                area = height * width
                max_area = max(area,max_area)
            stack.append(i)
        return max_area
        


