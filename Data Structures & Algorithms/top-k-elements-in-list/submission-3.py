import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = {}
        for char in nums:
            if char in mem:
                mem[char] +=1
            else:
                mem[char] = 1
        
        heap = []

        for key in mem:
            heapq.heappush(heap, (mem[key],key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]