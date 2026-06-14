class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_vol = 0
        while i < j:
            left = heights[i]
            right = heights[j]
            minimum = min(heights[i],heights[j])
            vol = (j-i)*(minimum)
            max_vol = max(vol,max_vol)
            if left < right:
                i+=1
            elif right<left:
                j-=1
            else:
                i+=1
                j-=1
        return max_vol
            
