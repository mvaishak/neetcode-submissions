import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        #Static window
        l = 0
        maxheap = []
        output = []

        for r in range(len(nums)):

            c = nums[r]
            heapq.heappush(maxheap,(-1*c,r))
            while maxheap[0][1] < l:
                heapq.heappop(maxheap)
            if r >= k -1:
                cur_max = maxheap[0][0] * -1 
                output.append(cur_max)
                l += 1
        return output 
            
            





        