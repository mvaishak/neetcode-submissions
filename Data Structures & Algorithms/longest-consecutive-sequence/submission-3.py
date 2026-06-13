import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap,i)

        cur = 0
        if len(heap)==0:
            return 0
        past = heapq.heappop(heap)
        cur_len = 1
        max_len = 1
        for _ in range(len(heap)):
            cur = heapq.heappop(heap)
            print(cur)
            if cur-past>1:
                cur_len = 1
                past = cur
            if cur == past:
                continue
            else:
                past = cur
                cur_len +=1
                max_len = max(max_len,cur_len)
        return max_len 

        