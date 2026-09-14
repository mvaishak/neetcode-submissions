class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area is l * b. To maximize, I need to find the combination that returns the best. I know its a two pointer and O(n) so single sweep through
        # As we sweep through, the moment we encounter val_j > val_i, we reset the base, until then we find every area with vali_i as start and compare with max_len.
        i = 0
        n=len(heights)
        j = n-1
        max_area = 0
        while (i<j):
            max_area = max(max_area, min(heights[i],heights[j])*(j-i))
            if heights[i] > heights[j]:
                j-=1
            elif heights[j] > heights[i]:
                i+=1
            else:
                i+=1
                j-=1
        return max_area
